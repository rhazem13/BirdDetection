import pandas as pd

def _extract_attrs_from_file(filename, attrs):
    if attrs == '*': 
        df = pd.read_csv(filename)
    else:
        df = pd.read_csv(filename, usecols=attrs)
    return df
