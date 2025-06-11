# 📊 Sales Data ETL Pipeline & Interactive Dashboard

This project demonstrates a simple ETL (Extract, Transform, Load) workflow using Python and SQLite as a data store, with an interactive Streamlit dashboard for data visualization. It's designed to showcase core data engineering and analytics concepts aligned with job descriptions involving ETL pipelines, SQL databases, and dashboard development.

---

## 📌 Project Overview

- **Extract:** Load sales data from a CSV file.
- **Transform:** Clean and compute new columns (like Total Amount).
- **Load:** Insert processed data into an SQLite database.
- **Visualize:** Build an interactive dashboard to explore total sales, top products, and sales by category using Streamlit.

---

## 📂 Project Structure

```bash
sales_data_pipeline/
├── data/
│   ├── sales_data.csv
├── etl_pipeline.py
├── requirements.txt
├── dashboard.py
└── README.md
