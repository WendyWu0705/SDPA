import requests
import pandas as pd

url = "https://data.stats.gov.cn/easyquery.htm"
params = {
    "m": "QueryData",
    "dbcode": "hgnd",      # monthly data
    "rowcode": "zb",
    "colcode": "sj",
    "wds": "[]",
    "dfwds": '[{"wdcode":"zb","valuecode":"A010101"}]'  # CPI indicator code
}

r = requests.get(url, params=params)
data = r.json()

# Parse JSON response
nodes = data['returndata']['datanodes']

records = []
for node in nodes:
    value = node['data']['data']
    time = node['wds'][1]['valuecode']   # time key, e.g. 202401
    records.append([time, value])

df = pd.DataFrame(records, columns=["日期", "CPI"])
df.to_csv('CPI.csv')
