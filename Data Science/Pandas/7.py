"""
Joins / Merges Customers  Orders)
    Create a customers DataFrame: customer_id , signup_date , segment .
    Merge with orders.
    Compute revenue by segment and retention proxy:
        “active in last 60 daysˮ per segment.
"""
import pandas as pd
from datetime import timedelta

df_customer=pd.read_csv("customers.csv")
df_order=pd.read_csv("orders.csv")

# checking data type of customer_id in customer data  (output : int64)
print("Data type of customer_id in customer data:\n",df_customer["customer_id"].dtype) 

# checking data type of customer_id in order data  (output : object)
print("Data type of customer_id in order data:\n",df_order["customer_id"].dtype)

df=pd.merge(df_customer,df_order, on="customer_id",how="inner")

print("Merger data:\n",df)


N=60
df["order_date"]=pd.to_datetime(df["order_date"],format="%Y-%m-%d")
start_date=df["order_date"].max() - timedelta(days=N)

orders_in_last_60days=df[df["order_date"]>start_date]



active_in_last_60days=(
    orders_in_last_60days.groupby("segment")
    .agg(Total_revenu=("net_amount","sum"), 
         active_customer=("customer_id","nunique")))



print("Active customers in last 60 days:\n",active_in_last_60days)

