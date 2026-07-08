# ================================
# WEEK 3 - SUPPLY CHAIN ANALYSIS
# TASK 3, 4, 5: EDA + ANALYSIS + CHARTS
# ================================

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Load dataset
df = pd.read_csv('SCMS Delivery History Dataset.csv')

# Date columns convert
date_cols = [
    'Scheduled Delivery Date',
    'Delivered to Client Date'
]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Numeric columns convert
df['Freight Cost (USD)'] = pd.to_numeric(df['Freight Cost (USD)'], errors='coerce')
df['Weight (Kilograms)'] = pd.to_numeric(df['Weight (Kilograms)'], errors='coerce')
df['Unit Price'] = pd.to_numeric(df['Unit Price'], errors='coerce')
df['Line Item Value'] = pd.to_numeric(df['Line Item Value'], errors='coerce')

# Fill missing values
df['Freight Cost (USD)'] = df['Freight Cost (USD)'].fillna(df['Freight Cost (USD)'].median())
df['Weight (Kilograms)'] = df['Weight (Kilograms)'].fillna(df['Weight (Kilograms)'].median())
df['Unit Price'] = df['Unit Price'].fillna(df['Unit Price'].median())

# ================================
# TASK 3: EDA
# ================================

print("=== SHIPMENT ANALYSIS ===")

# Most common shipment mode
print("\nMost Common Shipment Mode:")
print(df['Shipment Mode'].value_counts())

# Total shipments per country
print("\nTotal Shipments per Country (Top 10):")
print(df['Country'].value_counts().head(10))

print("\n=== DELIVERY PERFORMANCE ===")

# Delivery delay calculate karo
df['Delivery Delay'] = (
    df['Delivered to Client Date'] - df['Scheduled Delivery Date']
).dt.days

# Average delivery delay
print("\nAverage Delivery Delay (days):")
print(round(df['Delivery Delay'].mean(), 2))

# Delayed shipments
delayed = df[df['Delivery Delay'] > 0]
print("\nTotal Delayed Shipments:")
print(len(delayed))

print("\n=== COST ANALYSIS ===")

# Total Freight Cost
print("\nTotal Freight Cost (USD):")
print(round(df['Freight Cost (USD)'].sum(), 2))

# Average Line Item Value
print("\nAverage Line Item Value (USD):")
print(round(df['Line Item Value'].mean(), 2))

# ================================
# TASK 4: GROUP BASED ANALYSIS
# ================================

print("\n=== GROUP BASED ANALYSIS ===")

# Country vs total shipments
print("\nCountry vs Total Shipments (Top 5):")
print(df.groupby('Country')['ID'].count().sort_values(ascending=False).head(5))

# Vendor vs total cost
print("\nVendor vs Total Cost (Top 5):")
print(df.groupby('Vendor')['Freight Cost (USD)'].sum().sort_values(ascending=False).head(5))

# Product Group vs total value
print("\nProduct Group vs Total Value:")
print(df.groupby('Product Group')['Line Item Value'].sum().sort_values(ascending=False))

# Shipment Mode vs average delay
print("\nShipment Mode vs Average Delay (days):")
print(df.groupby('Shipment Mode')['Delivery Delay'].mean().round(2))

# ================================
# TASK 5: CHARTS
# ================================

# Chart 1: Bar Chart - Country vs Shipments
plt.figure(figsize=(12, 6))
country_shipments = df['Country'].value_counts().head(10)
plt.bar(country_shipments.index, country_shipments.values, color='steelblue')
plt.title('Top 10 Countries by Total Shipments')
plt.xlabel('Country')
plt.ylabel('Total Shipments')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart1_country_shipments.png')
plt.show()
print("Chart 1 saved!")

# Chart 2: Pie Chart - Shipment Mode Distribution
plt.figure(figsize=(8, 8))
shipment_mode = df['Shipment Mode'].value_counts().dropna()
plt.pie(shipment_mode.values,
        labels=shipment_mode.index,
        autopct='%1.1f%%',
        colors=['steelblue', 'orange', 'green', 'red'])
plt.title('Shipment Mode Distribution')
plt.tight_layout()
plt.savefig('chart2_shipment_mode.png')
plt.show()
print("Chart 2 saved!")

# Chart 3: Line Chart - Delivery Trend Over Time
plt.figure(figsize=(12, 6))
df['Delivery Month'] = df['Delivered to Client Date'].dt.to_period('M')
monthly_deliveries = df.groupby('Delivery Month')['ID'].count().dropna()
monthly_deliveries.index = monthly_deliveries.index.astype(str)
plt.plot(monthly_deliveries.index,
         monthly_deliveries.values,
         color='steelblue', marker='o', linewidth=2)
plt.title('Delivery Trend Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Deliveries')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart3_delivery_trend.png')
plt.show()
print("Chart 3 saved!")

print("\nAll Tasks Complete!")

# ================================
# INSIGHTS AND RECOMMENDATIONS
# ================================

print("\n=== 5 PYTHON ANALYSIS INSIGHTS ===")
print("""
1. Air is the most common shipment mode with 6,113 shipments (61.4% of total),
   showing that fast delivery is prioritized over cost in this supply chain.

2. South Africa has the highest shipments (1,406), followed by Nigeria (1,194)
   and Cote d'Ivoire (1,083), indicating these are the top delivery destinations.

3. Average delivery delay is -6.02 days, meaning most shipments arrive early
   before the scheduled delivery date, which shows good supply chain performance.

4. Total freight cost is $93 million across 10,324 shipments, with an average
   line item value of $157,650 per shipment.

5. Ocean shipments have the highest average delay of +5.87 days while Air Charter
   is the fastest with -19.04 days, showing significant difference between modes.
""")

print("=== 3 POWER BI DASHBOARD INSIGHTS ===")
print("""
1. Bar chart shows South Africa and Nigeria dominate shipment volume,
   together accounting for over 25% of all deliveries in the dataset.

2. Line chart shows delivery trend grew steadily from 2006 to 2014,
   with peak activity around mid-2014 showing business expansion over time.

3. Pie chart confirms Air (61.4%) is the dominant shipment mode,
   followed by Truck (28.4%), showing speed is preferred over cost savings.
""")

print("=== 2 BUSINESS RECOMMENDATIONS ===")
print("""
1. Reduce Ocean shipments where possible since they cause the most delays
   (+5.87 days average). Switch to Air or Truck for time-sensitive deliveries.

2. Focus supply chain resources on top countries (South Africa, Nigeria,
   Cote d'Ivoire) as they handle the highest volume and need more vendor support.
""")

print("All Insights Complete!")
