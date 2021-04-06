import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import pandas as pd
from pymongo import MongoClient
import datetime
import cx_Oracle 

df= pd.read_excel('C:\\Users\\sgunnala\\Desktop\\test2.xlsx', engine='openpyxl',usecols=['dealId','sku'])
v1=df['dealId'].tolist()
v1="','".join(set(map(str,v1)))
v1="('"+v1+"')"
print(v1)

v2=df['sku'].tolist()
v2="','".join(set(map(str,v2)))
v2="('"+v2+"')"
print(v2)
