import pandas as pd
from datetime import datetime,timedelta


df=pd.read_csv("orders.csv")
print("Data type of date:",df['order_date'].dtype)

df["order_date"]=pd.to_datetime(df["order_date"],format="%Y-%m-%d")
print("After changing the Data type of date :",df['order_date'].dtype)

categories = ["Electronics", "Fashion"]
X = 5000
N = 30

# computing start date to filter data
start_date=df["order_date"].max() - timedelta(days=N)

filtered_data=df[(df["category"].isin(categories)) & (df["net_amount"]>=X) & (df["order_date"]>=start_date)]

order_count=filtered_data.shape[0]
total_net_amount=filtered_data["net_amount"].sum()

print("Order count:",order_count)
print("Total net amount:",total_net_amount)
