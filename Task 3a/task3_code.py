import tabula
import pandas as pd
import json
import pymongo
from pymongo import MongoClient
from pprint import pprint
client = pymongo.MongoClient("mongodb+srv://user1:123@cluster0.ygzg9.mongodb.net/db1?retryWrites=true&w=majority")
mydb=client.test
file=input()
tables = tabula.read_pdf(file, output_format='dataframe', pages='all')
print("FILE ",file,"----------------")
for table in tables:
    print(table)
    d = json.loads(table.T.to_json()).values()
    #print(d)
    col=mydb[file]
    #col
    col.insert_many(d)
            

