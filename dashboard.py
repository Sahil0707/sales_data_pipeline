import streamlit as st
import sqlite3
import pandas as pd

# Connect to SQLite DB
conn = sqlite3.connect('sales.db')

# Load data
df = pd.read_sql_query("SELECT * FROM sales", conn)

# Streamlit UI
st.title("📊 Sales Data Dashboard")

st.subheader("Total Sales Amount")
st.metric("Total Revenue ($)", f"{df['TotalAmount'].sum():,.2f}")

st.subheader("Top 5 Products by Sales")
top_products = df.groupby('ProductName')['TotalAmount'].sum().sort_values(ascending=False).head(5)
st.bar_chart(top_products)

st.subheader("Sales by Category")
category_sales = df.groupby('Category')['TotalAmount'].sum()
st.bar_chart(category_sales)

st.subheader("Raw Sales Data")
st.dataframe(df)

conn.close()
