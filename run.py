import pandas as pd

#defining the file paths

raw_file_path = "Superstore-data.csv"
cleaned_file_path = "Superstore-data-cleaned.csv"

#defining functions

def load_data(file_path):

    #loading the raw data
    try:
        df = pd.read_csv(file_path, encoding="utf-8")
        print("File loaded successfully with UTF-8 encoding.")
    
    except UnicodeDecodeError as error:
        print("UTF-8 failed.")
        print("Error message:")
        print (error)

        print ("\nTrying again with latin1 encoding...")
        df = pd.read_csv(file_path, encoding='latin1')
        print("File loaded successfully with latin1 encoding.")

        print("Finished load_data()")
    
        print(f"Rows loaded: {df.shape[0]}")
    
        print(f"Columns loaded: {df.shape[1]}")
    
        print("First 5 rows:")
        print(df.head())

        print("\nData types when first loaded:")
        print(df.dtypes)

        print("\nSummary of numeric columns:")
        print(df.describe())

    return df

df = load_data(raw_file_path)

#cleaning the column names

def clean_column_names(df):
    print ("Column names before cleaning:")
    print(df.columns)

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-","_")
    )
    print ("column names after cleaning:")
    print (df.columns)

    return df

#Check data types before transformation
def check_and_transform_data_types(df):
    print("\nData types before transformation")
    print(df.dtypes)
          
    #convert postal_code to string
    df['postal_code'] = df['postal_code'].astype(str)

    #Convert date columns from object to datetime
    
    df["order_date"] = pd.to_datetime(df["order_date"], format="%m/%d/%Y")
    df["ship_date"] = pd.to_datetime(df["ship_date"], format="%m/%d/%Y")

    print("\nData types after transformation:")
    print(df.dtypes)

    return df

#Check for missing values in each column
def check_missing_values(df):
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    return df

#Check for duplicate rows
def check_duplicate_rows(df):
    print("\nNumber of duplicate rows:")
    print (df.duplicated().sum())

    return df

#Check that the shipping date is not before the order date
def check_shipping_dates(df):
    invalid_dates = df[df["ship_date"] < df["order_date"]]
    print("\nInvalid shipping dates (before order date):")
    print("\nRows where ship_date is before order_date")
    print(len(invalid_dates))

    return df

#Check whether key numeric columns contain sensible values
def check_numeric_values(df):
    print("\nNumeric summary:")
    print(df[["sales", "quantity", "discount", "profit"]].describe())

    print("\nRows with sales <= 0:")
    print((df["sales"] <= 0).sum())

    print("\nRows with quantity <= 0:")
    print((df["quantity"] <= 0).sum())

    print("\nRows with discount outside 0 to 1:")
    print(((df["discount"] < 0) | (df["discount"] > 1)).sum())

    return df

#Checking for outliers
def check_outliers(df):
    print("\n--- Checking for Outliers---")
    numeric_columns = ["sales", "quantity", "discount", "profit"]

    for column in numeric_columns: 
        print(f"\nChecking column: {column}")
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr= q3-q1
        
        lower_limit = q1 - 1.5*iqr
        upper_limit = q3 + 1.5*iqr

        outliers = df[(df[column] < lower_limit) | (df[column] > upper_limit)]

        print(f"Q1: {q1}")
        print(f"Q3: {q3}")
        print(f"IQR: {iqr}")
        print(f"Lower limit: {lower_limit}")
        print(f"Upper limit: {upper_limit}")
        print(f"Number of possible outliers: {len(outliers)}")

        if len(outliers) > 0:
            print("Example possible outliers:")
            print(outliers[[column]].head())

    return df

# running the functions

df = clean_column_names(df)
df = check_and_transform_data_types(df)
df = check_missing_values(df)
df = check_duplicate_rows(df)
df = check_shipping_dates(df)
df = check_numeric_values(df)
df = check_outliers(df)

print("\nFinal cleaned dataset shape:")
print(df.shape)

print("\nFinal column names:")
print(df.columns)

print("\nFinal data types:")
print(df.dtypes)


# Add calculated columns
df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days
df["profit_margin"] = df["profit"] / df["sales"]

print ("\nadded new calculaated columns:")

# Check that the new columns exist
print("\nColumns after adding calculated columns:")
print(df.columns)

print("\nPreview of calculated columns:")
print(df[["order_date", "ship_date", "shipping_days", "sales", "profit", "profit_margin"]].head())

# Save cleaned file AFTER adding calculated columns
df.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned file saved as: {cleaned_file_path}")

#Numpy exploration

import numpy as np

print("\n===Numpy Exploration of Cleaned Data ---")

#Investigating the main numerical columns 
#these are sales, quantity, discount and profit

#creating a numpy array for each numerical column
sales = df["sales"].to_numpy()
quantity = df["quantity"].to_numpy()
discount = df["discount"].to_numpy()
profit = df["profit"].to_numpy()

#calculating the key statistics for each column

