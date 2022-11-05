



from sql_metadata import Parser
from sql_metadata.compat import get_query_columns, get_query_tables
import pandas as pd

#def execute(query) : 

"""
    takes query as string
    returns: dictionary holds table name, and attributes
"""
def _parse(query):
    result = {'Tables: ':get_query_tables(query),'Columns':get_query_columns(query)} 
    return result

"""
    takes filename (string), and attributes(list)
    returns: list of rows
"""
def _extract_attrs_from_file(filename, attrs):
    if attrs == '*': 
        df = pd.read_csv(filename)
    else:
        df = pd.read_csv(filename, usecols=attrs)
    return df
    
