import pandas as pd

def clean(input_file):
    df=pd.read_csv(input_file)
    return df

