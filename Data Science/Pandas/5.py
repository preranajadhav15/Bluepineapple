import pandas as pd

#read csv file
df=pd.read_csv("orders.csv")
df.head()

# checking data type of order_date
print("Data type of date:",df['order_date'].dtype)

# changing data type of order_date ti datetime to extract month
df["order_date"]=pd.to_datetime(df["order_date"],format="%Y-%m-%d")

print("After changing the Data type of date :",df['order_date'].dtype)

#extracting month from order_date
df["month"]=df["order_date"].dt.month_name()
print(df["month"])

# creating pivot table
pivot=(pd.pivot_table(df,index="month",columns="category",values="net_amount",aggfunc="sum",fill_value=0,sort=False))
print("Created Pivot:\n",pivot)

# computing grand total month wise
pivot["Grand Total"]=pivot.sum(axis=1)
print("Pivot after adding grand total:\n",pivot)

# Growth percentage month over month
pivot["Month over Month Growth %"]=pivot["Grand Total"].pct_change()*100
pivot["Month over Month Growth %"]=pivot["Month over Month Growth %"].fillna(0)
print("Month over month growth:\n",pivot)