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
```
## 🛠 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Sahil0707/sales-data-pipeline.git
   cd sales-data-pipeline

2. Create a virtual environment and activate it:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate     # Windows
3. Install Dependencies:
   ```sh
   pip install -r requirements.txt
   
4. Run the ETL Pipeline
   ```sh
   python etl_pipeline.py

6. Run the streamlit dashboard
   ```sh
   streamlit run dashboard.py

## 📈 Features
- Extract, Transform, and Load (ETL) sales data into a relational database.
- Visualize Total Revenue, Top Performing Products, and Sales by Category.
- Interactive dashboard built with Streamlit.
- Clean, scalable structure for future integration with cloud tools like AWS RDS, Snowflake, AWS Glue, or Airflow.

## 📚 Tech Stack
Python
SQLite
Pandas
Streamlit
SQL

## 📌 Future Improvements
- Integrate with AWS RDS or Snowflake instead of SQLite.
- Automate the ETL workflow using Apache Airflow.
- Deploy the Streamlit app on cloud services.
