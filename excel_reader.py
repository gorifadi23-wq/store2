import pandas as pd

def read_excel_file(path):
    df = pd.read_excel(path)
    data = df.values.tolist()
    return data
