import pandas as pd
import numpy as np
from datetime import datetime
import boto3

df = pd.read_csv(r"C:\Users\rohit\Downloads\MSFT.csv", parse_dates=['Date'])

def format_data(dataframe,stock):
    renamed_columns = {"Date":"date", "Open":"open", "Close":"close", "High":"high", "Low":"low", "Adj Close":"adj_close", "Volume":"volume"}
    dataframe.rename(columns=renamed_columns, inplace = True)
    dataframe['index'] = stock+df['date'].dt.strftime("%d%m%y")
    dataframe['stock'] = stock
    dataframe.set_index('index', inplace = True)
    
def upload_file(file_name, bucket,object_name=None):
    print(file_name)
    if(object_name == None):
        object_name = file_name.split("/")[2]
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

format_data(df,"MSFT")
file_name = datetime.now().strftime("%d-%m-%Y")
file_path =  "./datafiles/{}.csv".format(file_name)
print(file_path)   
df.to_csv(file_path, encoding = 'utf-8')

upload_file(file_path,"stockarroni")