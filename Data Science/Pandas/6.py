"""
Handling Missing Values
    Randomly introduce missing values in city, payment_mode, and discount_pct.
    Apply different strategies:
        fill categorical with “Unknownˮ
        fill numeric with median by category
    Prove it worked: show missing counts before/after
"""

import pandas as pd
import numpy as np

df=pd.read_csv("orders.csv")
print("Data:\n",df)

#randomly missing values in city,payment_mode and discount_pct
df.loc[df.sample(frac=0.2).index,"city"]=np.nan
df.loc[df.sample(frac=0.1).index,"payment_mode"]=np.nan
df.loc[df.sample(frac=0.3).index,"discount_pct"]=np.nan

print("Data after adding random nan values:\n",df)

# fill categorical with unknown
categorical_data=df.select_dtypes(include="object").columns
df[categorical_data]=df[categorical_data].fillna("Unknown")

# fill numeric with median of category
df["discount_pct"]=(df.groupby("category")["discount_pct"].transform(lambda x : x.fillna(x.median())))

print("Data after filling the nan values:\n",df)