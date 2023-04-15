import json
import pandas as pd
import requests
from datetime import datetime
from simple_salesforce import Salesforce
from io import StringIO

with open('credentials.json') as f:
    credentials = json.load(f)

# LOGIN CREDENTIALS
username = credentials['email']  # Put your e-mail
password = credentials['password']  # Put your password
security_token = credentials['security_token']  # Put your token. You can get on configurations in salesforce

sf = Salesforce(username=username, password=password, security_token=security_token)
sessionId = sf.session_id
start_time = datetime.now()

# report URL structure

orgParams = 'https://<YOUR COMPANY>.my.salesforce.com/'  # you can see this in your Salesforce URL
exportParams = '?isdtp=p1&export=1&enc=UTF-8&xf=csv'

# DOWNLOAD
reportId = ''  # Choose the report and get the id

reportUrl = orgParams + reportId + exportParams
reportReq = requests.get(reportUrl, headers=sf.headers, cookies={'sid': sf.session_id})
reportData = reportReq.content.decode('utf-8-sig')
reportReadCsv = pd.read_csv(StringIO(reportData))

reportReadCsv.to_csv('./NAME.csv')

end_time = datetime.now()
print(f'Donwload Complete. Duration: {end_time - start_time}')
