import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Olist Sales Dashboard", page_icon="📊", layout="wide")
st.title("📊 Brazilian E-Commerce Sales Dashboard")
st.write("Interactive analysis of 100,000+ real orders from Olist")

# Connect to database
conn = sqlite3.connect('data/olist.db')

# ── Metric Cards ──
st.header("Key Metrics")

total_revenue = pd.read_sql_query("""
    SELECT ROUND(SUM(payment_value), 2) as revenue 
    FROM payments
""", conn).iloc[0]['revenue']

total_orders = pd.read_sql_query("""
    SELECT COUNT(DISTINCT order_id) as orders 
    FROM orders 
    WHERE order_status = 'delivered'
""", conn).iloc[0]['orders']

total_customers = pd.read_sql_query("""
    SELECT COUNT(DISTINCT customer_id) as customers 
    FROM customers
""", conn).iloc[0]['customers']

avg_review = pd.read_sql_query("""
    SELECT ROUND(AVG(review_score), 2) as avg_score 
    FROM reviews
""", conn).iloc[0]['avg_score']

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"R$ {total_revenue:,.0f}")
col2.metric("Delivered Orders", f"{total_orders:,}")
col3.metric("Total Customers", f"{total_customers:,}")
col4.metric("Avg Review Score", f"{avg_review} / 5")

st.divider()

# ── Revenue Over Time ──
st.header("Revenue Over Time")

revenue_data = pd.read_sql_query("""
    SELECT 
        strftime('%Y-%m', o.order_purchase_timestamp) AS month,
        ROUND(SUM(p.payment_value), 2) AS total_revenue
    FROM orders o
    JOIN payments p ON o.order_id = p.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY month
    ORDER BY month
""", conn)

fig1 = px.line(revenue_data, x='month', y='total_revenue',
               title='Monthly Revenue',
               labels={'month': 'Month', 'total_revenue': 'Revenue (BRL)'})
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# ── Top Categories ──
col_left, col_right = st.columns(2)

with col_left:
    st.header("Top 10 Categories by Revenue")
    cat_data = pd.read_sql_query("""
        SELECT 
            ct.product_category_name_english AS category,
            ROUND(SUM(oi.price), 2) AS total_revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        JOIN category_translation ct ON p.product_category_name = ct.product_category_name
        GROUP BY category
        ORDER BY total_revenue DESC
        LIMIT 10
    """, conn)
    fig2 = px.bar(cat_data, x='total_revenue', y='category',
                  orientation='h',
                  labels={'total_revenue': 'Revenue (BRL)', 'category': 'Category'})
    st.plotly_chart(fig2, use_container_width=True)

with col_right:
    st.header("Top 10 States by Customers")
    state_data = pd.read_sql_query("""
        SELECT 
            customer_state AS state,
            COUNT(DISTINCT customer_id) AS total_customers
        FROM customers
        GROUP BY state
        ORDER BY total_customers DESC
        LIMIT 10
    """, conn)
    fig3 = px.bar(state_data, x='total_customers', y='state',
                  orientation='h',
                  labels={'total_customers': 'Customers', 'state': 'State'})
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ── Review Scores ──
st.header("Average Review Score by Category")
review_data = pd.read_sql_query("""
    SELECT 
        ct.product_category_name_english AS category,
        ROUND(AVG(r.review_score), 2) AS avg_score,
        COUNT(r.review_id) AS total_reviews
    FROM reviews r
    JOIN orders o ON r.order_id = o.order_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    JOIN category_translation ct ON p.product_category_name = ct.product_category_name
    GROUP BY category
    HAVING total_reviews > 100
    ORDER BY avg_score DESC
    LIMIT 10
""", conn)
fig4 = px.bar(review_data, x='avg_score', y='category',
              orientation='h',
              color='avg_score',
              color_continuous_scale='RdYlGn',
              labels={'avg_score': 'Avg Review Score', 'category': 'Category'})
st.plotly_chart(fig4, use_container_width=True)

conn.close()