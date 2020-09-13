import boto3

s3 = boto3.resource('s3')
obj = s3.Object('mydatabucket5','auto-mpg.csv')
obj.download_file(r"C:\Users\rohit\stock_forecasting\dataload\temp")