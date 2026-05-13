# Superstore-data-analysis


# Project Overview

This project uses Python to clean, explore and visualise a Superstore's Sales dataset.

The aim of the project is to prepare the dataset for further analysis by checking data quality, transforming key columns, creating new calculated fields, exploring numerical patterns using NumPy, and visualising important findings using Matplotlib.

The cleaned dataset is exported as a new CSV file called:
Superstore-data-cleaned.csv

# Libraries used
Pandas - Used to load, clean and manipulate the dataset
Numpy - Used to explore the data and statistical analysis
Matplotlib - Used to create visualisations

# Dataset
The original dataset is loaded from:

Superstore-data.csv

The cleaned version is saved as: 
Superstore-data-cleaned.csv

The dataset contains sales order information, including fields such as 
- Order Date
- Ship Date
- Ship Mode
- Sales
- Quantity
- Discount
- Profit
- Product Category
- Region
- Customer Information

# Project Structure
The project follows these main stages:
1. Load the raw dataset
2. Clean the column names
3. Convert the data types
4. Check for missing values
5. Check for duplicate rows
6. Validate shipping dates
7. Check numeric values
8. Identify possible outliers
9. Add calculated columns
10. Explore the data using NumPy
11. Visualise key finidngs using Matplotlib
12. Export the cleaned dataset

# Data Cleaning Steps
1. Loading the Data set:
The dataset is loaded using pandas.read_csv()

The script first attempts to load the file using UTF-8 encoding. If this fails, it attempts to load the file using latin1 encoding.

2. Column Name Cleaning:
Column names are cleaned by 
a. removing extra spaces
b. converting names to lowercase
c. replacing spaces with underscores
d. replacing hyphens with underscores

for example: 
Order Date
becomes
order_date

3. Transforming Data Types:
The script converts important columns into more suitable data types.
The postal_code column is converted to a string because postal codes should not be treated as numbers.
The date columns are converted to datetime format:

order_date
ship-date

This allows the script to calculate the number of days between the orderdate and the shipping date. 

4. Checking Missing Values
The script checks each column for missing values using

df.isnull().sum()

This helps identify whethere any columns contains incomplete data

5. Checking Duplicate Rows

The script checks for duplicate rows using

df.duplicated().sum()

Duplicate records could affect the accuracy of the analysis so this is a quality assurance step. 

6. Checking Shipping Dates

The script checks whether any orders have a shipping date before the order date.
This would indicate an invalid date entry.

7. Checking Numeric Values

The script checks whether the main numeric columns contain sensible values.

The columns checked are:
sales
quantity
discount
profit

The script checks for:

sales values less than or equal to zero
quantity values less than or equal to zero
discount values outside the range 0 to 1

8. Checking for Outliers

The script uses the IQR method to identify possible outliers

The columns checked are
sales
quantity
discount
profit

The IQR method calculates:
IQR = Q3-Q1

Values below the lower limit or above the upper limit are flagged as possible outliers. 

Outliers are not being automatically removed because they may represent genuine business activity, such as very large orders or unusually high losses.

# Calculated Columns

Two new calculated columns are added to the data set. 

1. Shipping Days

This is calculated by:

shipping_days = ship_date - order_date

This calculates the number of days it takes from ordering to dispatch

This can be used to analyse delivery performance by shipping method

2. Profit Margin

This is calculated by: 

df["profit_margin"] = df["profit"] / df["sales"]

This calculates the profit made as a proportion of sales.

Profit margin is useful because it gives a better measure of profitability than profit alone, for example, a large order may have high profit but a low profit margin.

# Numpy Exploration

NumPy is used to explore the main numerical columns in the cleaned dataset.

The columns analysed are:
sales
quantity
profit
discount
shipping_days
profit_margin

For each column, the script calculates:
mean
median
standard deviation
minimum value
maximum value
25th percentile
50th percentile
75th percentile
90th percentile
95th percentile
99th percentile

This helps describe the spread of values and identify whether the data contains unusual or extreme values.

# Why were percentiles used?

Percentiles help describe the distribution of the data without relying only on the mean.

This is useful because columns such as sales and profit may contain outliers.

For example, a small number of very large sales could increase the mean, making it less representative of a typical order.

Percentiles help show what most orders look like and where unusually large or small values begin.

# Matplotlib Visualisations

Matplotlib is used to visualise important findings from the Numpy Exploration

1. Sales Distribution
A histogram is beign used to show the distribution of sales values.

The chart includes:
a mean sales line
a median sales line

This helps show whether sales are evenly distributed or skewed by a small number of high-value orders.

2. Profit Distribution
A histogram is used to show the distribution of profit values.

A break-even line is added at zero.

Orders to the left of this line are loss-making orders, while orders to the right are profitable.

3. Loss Rate by Discount Level

A bar chart is used to show the percentage of loss-making orders at each discount level.

This helps investigate whether higher discounts are associated with a greater chance of making a loss.

4. Average Shipping Time by Ship Mode

A bar chart is used to compare average shipping time across different shipping modes.

This helps evaluate whether faster shipping methods are performing as expected.

