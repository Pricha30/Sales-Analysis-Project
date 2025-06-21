# Step1: Import Libraries & Load Data

# importing necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# loading the dataset
df = pd.read_csv("C:\\Numpy for Data Science\\sales_data_sample.csv",encoding ='latin1')

# prieview the top 5 rows
print(df.head())

#Step 2:Explore the Data 

#basic info about the data.
print(df.info())

#checking the missing values
print(df.isnull())
print(df.isnull().sum())

# Step 3: Data Cleaning 

# 2. Replace inf/-inf with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# 3. Drop rows only if key columns are missing
df.dropna(subset=['SALES', 'ORDERDATE', 'QUANTITYORDERED', 'PRODUCTLINE'], inplace=True)

# Convert Date column to datetime
df["ORDERDATE"] = pd.to_datetime(df['ORDERDATE'])

df["Month"] = df["ORDERDATE"].dt.month
df["Year"] = df["ORDERDATE"].dt.year

"""
check column names --- df.columns- will show all the columns,
.strstrip---remove the extra spaces, str.lower----convert the column name to lowercase 
.str.replce('','_') will change year id to year_id

"""
print("Columns before cleaning:", df.columns.tolist()) 
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("Columns After cleaning:", df.columns.tolist()) 

# drop duplicate columns
df.drop_duplicates(inplace = True)

# Reset index
df.reset_index(drop=True, inplace=True)

#preview clean records
df.head()
df.info()

# Step 4: Summary Statistics for Key Columns
print("Summary Statistics:")
print(df[['sales', 'quantityordered']].describe())

# Mean and Standard Deviation Calculations
mean_sales = df['sales'].mean()
std_sales = df['sales'].std()
mean_qty = df['quantityordered'].mean()
std_qty = df['quantityordered'].std()

print(f"Mean Sales: ₹{mean_sales:.2f}")
print(f"Standard Deviation in Sales: ₹{std_sales:.2f}")
print(f"Mean Quantity Ordered: {mean_qty:.2f}")
print(f"Standard Deviation in Quantity Ordered: {std_qty:.2f}")

# Step 5: sales Analysis

#revenue
total_revenue = df["sales"].sum()
print(f"Total Revenue Generated:₹{total_revenue}")

#total quantity sold
total_quantity_sold = df["quantityordered"].sum()
print(f"Total Quantity sold:{total_quantity_sold}")

#top 5 products by revenue
top_products = df.groupby("productline")["sales"].sum().sort_values(ascending= False).head(5)
print("Top 5 products by revenue: \n",top_products)

#top 5 products plot
plt.figure(figsize=(8, 6))
top_products.plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Top 5 Product Lines by Revenue')
plt.ylabel('')  # Hides y-axis label
plt.tight_layout()
plt.show()


# monthly revenue trend
monthly_revenue = df.groupby("month")["sales"].sum().sort_index()
print("Monthly revenue Trends: \n", monthly_revenue)

#revenue trends plot
monthly_revenue.plot(kind='line', marker='o', title='Monthly Sales Trend', color='green')
plt.xlabel('Month')
plt.ylabel('Revenue (₹)')
plt.grid(True)
plt.tight_layout()
plt.show()
print("The sales were at peak around november")

# Monthly Sales Standard Deviation
monthly_std = df.groupby('month')['sales'].std()
print("Monthly Sales Standard Deviation:\n", monthly_std)

#Sales by Region (Country)
country_sales = df.groupby('country')['sales'].sum().sort_values(ascending=False)
print("Countries by Sales:\n",country_sales)

#Top 10 country by sales plot
top_countries = country_sales.head(10)

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
top_countries.plot(kind='barh', color='skyblue')

plt.xlabel('Total Sales (₹)')
plt.ylabel('Country')
plt.title('Top 10 Countries by Sales Revenue')
plt.gca().invert_yaxis()  # Highest at top
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# cleaned and visualized data
df.to_csv("Cleaned_sales_sample_data.csv",index = False)


"""
Insight Summary:
- Average sale value: ₹3,553.89, with a standard deviation of ₹1,841.87
- Quantity ordered averages 35.09 units, with a standard deviation of 9.74 units
- Monthly sales trends show significant variation, with peak sales occurring in November
"""