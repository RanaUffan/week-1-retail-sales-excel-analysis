# week-1-retail-sales-excel-analysis

## Project Title
Retail Sales & Supply Chain Data Analysis — LogicStack Data Analysis Internship

## Project Objective
This project covers 3 weeks of data analysis tasks completed during the 
LogicStack Data Analysis Internship (June-July 2026). It progresses from 
basic Excel analysis to advanced Python and Power BI dashboard creation.

## Tools Used
- Microsoft Excel / Google Sheets
- Power BI Desktop
- Python (Pandas, Matplotlib)
- GitHub

## Week 1 — Excel Data Cleaning & Basic Analysis

### Dataset
retail_sales_dataset.csv — 1,000 retail transactions, 9 columns

### Work Completed
- Opened and explored the dataset structure
- Cleaned and formatted data (bold headers, date format, currency format)
- Checked data quality (blank cells, duplicates, valid values)
- Added Calculated Total and Amount Check columns using formulas
- Calculated key metrics using SUM, AVERAGE, MIN, MAX, COUNT
- Created summary tables using SUMIF
- Applied sorting and filtering with screenshots
- Built Bar, Column, and Pie charts
- Written observations based on analysis

### Excel Sheets
1. Original Data
2. Cleaned Data
3. Dataset Understanding
4. Data Quality Check
5. Basic Analysis
6. Sorting and Filtering Screenshots
7. Charts
8. Observations

### Key Observations
1. Electronics had the highest total sales (Rs. 156,905), slightly ahead
   of Clothing (Rs. 155,580), while Beauty had the lowest (Rs. 143,515).
2. Beauty had the lowest sales even though quantity sold was close
   to other categories.
3. Female customers generated more total sales (Rs. 232,840) than
   male customers (Rs. 223,160).
4. Customer ages range from 18 to 64, showing a wide adult customer base.
5. The highest single transaction was Rs. 2,000, much higher than
   the average sale of Rs. 456.

---

## Week 2 — Advanced Excel + Power BI Dashboard

### Dataset
Same retail_sales_dataset.csv from Week 1

### Work Completed
- Created 4 Pivot Tables:
  - Total Sales by Product Category
  - Total Sales by Gender
  - Total Quantity by Product Category
  - Average Age by Product Category
- Calculated 6 KPIs in Excel:
  - Total Sales: Rs. 456,000
  - Total Transactions: 1,000
  - Average Sales: Rs. 456
  - Total Quantity Sold: 2,514
  - Highest Transaction Value: Rs. 2,000
  - Lowest Transaction Value: Rs. 25
- Written 5 business insights
- Built interactive Power BI Dashboard

### Power BI Dashboard
- KPI Cards: Total Sales, Total Transactions, Average Sales, Total Quantity
- Bar Chart: Sales by Product Category
- Pie Chart: Sales by Gender
- Column Chart: Quantity Sold by Category
- Line Chart: Sales Trend Over Time

### Key Insights
1. Electronics is the strongest category with total sales of Rs. 156,905.
2. Beauty had the lowest sales despite reasonable quantity sold (771 units).
3. Female customers are stronger buying segment (Rs. 232,840 vs Rs. 223,160).
4. Average customer age is around 41 years — middle-aged adult base.
5. Wide transaction range from Rs. 25 to Rs. 2,000 shows diverse behavior.

---

## Week 3 — Supply Chain Analytics (Python + Power BI)

### Dataset
SCMS_Delivery_History_Dataset.csv — 10,324 records, 33 columns

### Work Completed
- Loaded and explored supply chain dataset using Python Pandas
- Cleaned data: converted dates, handled missing values, fixed numeric columns
- Performed EDA: shipment analysis, delivery performance, cost analysis
- Group-based analysis: Country, Vendor, Product Group, Shipment Mode
- Created 3 Python charts (Bar, Pie, Line) using Matplotlib
- Built Power BI Supply Chain Performance Dashboard

### Power BI Dashboard
- Title: Supply Chain Performance Dashboard
- KPI Cards: Total Shipments, Total Freight Cost, Average Delivery Delay,
  Total Line Item Value
- Bar Chart: Country vs Total Shipments
- Line Chart: Delivery Trend Over Time
- Pie Chart: Shipment Mode Distribution
- Column Chart: Vendor vs Total Cost

### Key Insights
1. Air is most common shipment mode (61.4% of total shipments), showing
   speed is prioritized over cost.
2. South Africa has highest shipments (1,406), followed by Nigeria (1,194).
3. Average delivery delay is -6.02 days meaning shipments arrive early.
4. Total freight cost is $93 million across 10,324 shipments.
5. Ocean shipments have highest delay (+5.87 days) while Air Charter
   is fastest (-19.04 days).

### Business Recommendations
1. Reduce Ocean shipments where possible — switch to Air or Truck for
   time-sensitive deliveries to avoid delays.
2. Focus supply chain resources on top countries (South Africa, Nigeria)
   as they handle highest volume and need more vendor support.

---

## Note for Viewers
This repository contains my Week 1, 2, and 3 submissions for the 
LogicStack Data Analysis Internship. Each week builds on the previous 
one — from basic Excel to advanced Python and Power BI dashboards. 
All files are organized by week for easy review.
