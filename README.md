# 📊 Stock Data Pipeline & Analytics Dashboard

## 🚀 Overview

An end-to-end data engineering and analytics project that ingests stock market data from the Yahoo Finance API, processes and stores it in PostgreSQL, and visualizes insights through an interactive Power BI dashboard.

---

## 🏗 Architecture

```
Yahoo Finance API → Python ETL → PostgreSQL → Power BI Dashboard
```

---

## 🛠 Tech Stack

* **Python** (Pandas, yfinance)
* **PostgreSQL** (data storage)
* **SQLAlchemy** (DB connection)
* **Power BI** (visualization)
* **Git & GitHub** (version control)

---

## ⚙️ Key Features

* Automated stock data ingestion (intraday intervals)
* Data cleaning & transformation pipeline (ETL)
* Relational storage in PostgreSQL
* Time-series analysis and visualization
* Financial indicators:

  * Moving Averages (MA20, MA50)
  * Daily Return (%)
  * Bullish / Bearish signal detection
* Interactive dashboard with filters and KPIs

---

## 📊 Dashboard Highlights

* 📈 **Price Trend with Moving Averages**
* 📊 **Trading Volume Analysis**
* 📉 **Daily Return (%)**
* 🔔 **Signal Indicator (Bullish/Bearish)**
* 🎛 **Dynamic Time Filtering**

---

## 📸 Dashboard Preview

![Dashboard](dashboard.png)

---

## 🧪 How to Run

### 1. Clone repository

```
git clone https://github.com/shreeharsh24/stock-data-pipeline-dashboard.git
cd stock-data-pipeline-dashboard
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Configure database

Update `config.py` with your PostgreSQL credentials.

### 4. Run pipeline

```
python main.py
```

---

## 📁 Project Structure

```
Pipeline_project/
│
├── etl.py                # Extract + Transform logic
├── db.py                 # Database connection
├── config.py             # Configuration (DB, symbols)
├── main.py               # Pipeline runner
├── requirements.txt
├── .gitignore
│
├── dashboard/
│   └── stock price analysis dashboard.pbix
│
└── dashboard.png         # Dashboard preview
```

---

## 🧠 Key Learnings

* Designed a modular ETL pipeline for real-world data ingestion
* Handled time-series data transformations and schema normalization
* Integrated backend data systems with BI tools
* Built financial analytics features (MA, returns, signals)

---

## 🎯 Future Improvements

* Multi-stock comparison
* Pipeline scheduling (Airflow / cron)
* Real-time streaming (Kafka / Spark)
* API layer (FastAPI)

---

## 📌 Resume Summary

Built an end-to-end stock data pipeline using Python, PostgreSQL, and Power BI, implementing financial analytics such as moving averages, return metrics, and trading signals for interactive visualization.

---

## 📄 License

This project is for educational and portfolio purposes.
