# 📊 Brazilian E-Commerce Sales Dashboard

An interactive business intelligence dashboard analyzing 100,000+ real 
orders from Olist, Brazil's largest e-commerce platform. Built with 
SQL, Python, and Streamlit.

## 🔗 Live Demo
[Click here to view the dashboard](YOUR_STREAMLIT_LINK)

## 📌 Problem Statement
E-commerce businesses generate massive amounts of order data but 
struggle to extract actionable insights. This dashboard transforms 
raw transactional data into clear business metrics using SQL queries 
and interactive visualizations.

## 📊 Key Insights Found
- Total platform revenue: **R$ 16,008,872** across 96,478 delivered orders
- **São Paulo** dominates with 40,000+ customers — 4x more than any other state
- **Health & Beauty** is the top revenue category at over R$ 1M
- Revenue grew **5x** from late 2016 to peak in late 2017
- Average customer review score: **4.09 / 5** across all categories
- **Computers** and **Home Appliances** have the highest satisfaction scores

## 🛠 Tech Stack
| Tool | Purpose |
|---|---|
| Python | Core language |
| SQL (SQLite) | Data extraction and aggregation |
| Pandas | Data manipulation |
| Plotly | Interactive visualizations |
| Streamlit | Web dashboard deployment |

## 📁 Dataset
- Source: Brazilian E-Commerce Public Dataset by Olist (Kaggle)
- Size: 100,000+ orders from 2016 to 2018
- Tables: Orders, Customers, Products, Payments, Reviews, Sellers

## 🔍 SQL Queries Used
- Monthly revenue aggregation with JOIN across orders and payments
- Top 10 product categories by total revenue
- Customer distribution across Brazilian states
- Average review score by category (filtered for statistical significance)

## 📂 Project Structure
sales-dashboard/
├── data/
│   ├── olist_orders_dataset.csv
│   ├── olist_customers_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   ├── product_category_name_translation.csv
│   └── olist.db
├── notebooks/
│   └── analysis.ipynb
├── app.py
└── requirements.txt

## 🚀 Run Locally
pip install -r requirements.txt
streamlit run app.py

## 💡 Business Recommendations Based on Analysis
- Focus marketing spend in São Paulo — highest customer concentration
- Expand Health & Beauty and Watches & Gifts inventory — top revenue drivers
- Investigate late 2017 revenue spike for repeatable growth strategies
- Books category needs quality improvement — lowest review scores

## 👤 Author
Amuruth R
[LinkedIn](your-linkedin-link) | [GitHub](https://github.com/Amuruth6)
