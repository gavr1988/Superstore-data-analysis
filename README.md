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