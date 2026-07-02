# Project Architecture

## Architecture Overview

The Enterprise Sales Analytics Platform follows a modern ETL-based data analytics architecture.

```
                CSV Datasets
                     │
                     ▼
             Python ETL Pipeline
                     │
                     ▼
            PostgreSQL Database
                     │
      ┌──────────────┴──────────────┐
      ▼                             ▼
   SQL Analytics             Power BI Dashboard
      ▼                             ▼
 Business Insights        Executive Reporting
```

---

## Data Sources

- Customers Dataset
- Employees Dataset
- Products Dataset
- Orders Dataset
- Order Items Dataset
- Payments Dataset

---

## ETL Process

### Extract
- Read CSV files using Pandas.

### Transform
- Clean missing values.
- Generate employee email addresses.
- Generate phone numbers.
- Convert department names into department IDs.
- Validate relationships between tables.
- Prepare data for loading.

### Load
- Insert transformed data into PostgreSQL using SQLAlchemy.

---

## Database Schemas

### Customer Schema
- Customers

### Common Schema
- Employees

### Inventory Schema
- Products

### Sales Schema
- Orders
- Order Items

### Finance Schema
- Payments

---

## Analytics Layer

Business analysis is performed using SQL queries to calculate:

- Revenue Analysis
- Customer Analysis
- Product Analysis
- Sales Performance
- Payment Analysis
- Warehouse Performance
- Monthly Sales Trends

---

## Visualization Layer

Power BI dashboard displays:

- KPI Cards
- Sales Trend
- Customer Segments
- Revenue Analysis
- Product Performance
- Warehouse Performance
- Payment Insights

---

## Tools Used

- PostgreSQL
- Python
- Pandas
- SQLAlchemy
- SQL
- Power BI
- GitHub