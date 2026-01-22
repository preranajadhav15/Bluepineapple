"""
Window Functions Intermediate)
    For each customer:
        sort by order_date 
        compute prev_order_date
        compute days_since_prev
        compute rolling 3-order average net_amount 
    Identify customers whose average order value is increasing (simple heuristic)
"""

import pandas as pd


df=pd.read_csv("orders.csv")

sort_by_order_date=df.sort_values("order_date")
print(df)

df["order_date"]=pd.to_datetime(df["order_date"],format="%Y-%m-%d")

df["prev_order_date"]=(df.groupby("customer_id")["order_date"].shift(1))

df["days_since_prev"]=df["order_date"]-df["prev_order_date"]

df["rolling_3_orders"]=(df.groupby("customer_id")["net_amount"].transform(lambda x: x.rolling(window=3,min_periods=1).mean()))


avg_order=(df.groupby("customer_id")["rolling_3_orders"].agg(first_avg="first",last_avg="last"))

avg_order["is_increasing"]= avg_order["last_avg"]>avg_order["first_avg"]

print(avg_order)

increasing_customer=avg_order[avg_order["is_increasing"]]

print(df.dropna())
print(increasing_customer)