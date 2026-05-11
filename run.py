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

    print ("n\Trying again with latin1 encoding...")
    df = pd.read_csv(file_path, encoding='latin1')
    print ("File loaded successfully with latin 1 encoding.")
    return df

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
