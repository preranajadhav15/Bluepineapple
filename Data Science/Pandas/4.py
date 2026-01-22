#GroupBy Aggregations


import pandas as pd

#read csv
df=pd.read_csv("orders.csv")
df.head() # show first 5 rows of data

#Group by city and compute:total orders,unique customers,total revenue (sum net_amount),average order value
city_details=(
    df.groupby("city")
    .agg
    (total_orders=("order_id","count"),
     unique_customer=("customer_id","nunique"),
     total_revenue=("net_amount","sum"),
     avg_order_value=("net_amount","mean")
     ))

#sorting cities by revenu in descending order
city_details=city_details.sort_values(by="total_revenue",ascending=False)

# Showing sorted top 10 cities 
top_10_cities=city_details.head(10)
print("Top 10 cities are:\n",top_10_cities)

