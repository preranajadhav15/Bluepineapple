#Add Derived Columns

import pandas as pd

#read csv file
df=pd.read_csv("orders.csv")

# Using quantity , unit_price , discount_pct :
    #compute gross_amount = quantity * unit_price 
df["gross_amount"]=df["quantity"]*df["unit_price"]

    #compute net_amount = gross_amount * (1-discount_pct/100)
df["net_amount"]=df["gross_amount"]*(1-df["discount_pct"]/100)

#Add a is_high_value flag (net_amount > threshold ).
threshold=10000
df["is_high_value"]=df["net_amount"]>threshold

print(df)
df.to_csv("orders.csv")