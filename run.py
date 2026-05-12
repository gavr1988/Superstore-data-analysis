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
          

