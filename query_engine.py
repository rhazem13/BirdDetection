

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
#-> dict{table, cols}
#test
#_parse("SELECT COUNT(*) as cnt FROM dbo.main_table WHERE (VKRKA10001920015 = 1 AND age IN (15, 16, 17, 18, 19) AND income IN (101, 102, 301, 302, 305))")
"""
    takes filename (string), and attributes(list)
    returns: list of rows
"""
#def _extract_attr_from_file(filename, attr):
    
