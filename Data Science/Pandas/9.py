"""
    Outlier Detection  Capping Intermediate)
        For each category:
            compute IQR of net_amount
            flag outliers (outside [Q1-1.5IQR, Q3=1.5IQR])
            cap outliers to bounds (winsorize)
    Report outlier counts by category before/after
"""
import pandas as pd

df=pd.read_csv("orders.csv")
quantiles_data=(
    df.groupby("category")["net_amount"]
    .agg(Q1=(lambda x:x.quantile(0.25)),
         Q3=(lambda x:x.quantile(0.75))))

quantiles_data["IQR"]=quantiles_data["Q3"]-quantiles_data["Q1"]
print(quantiles_data)

quantiles_data["lower_bound"]=quantiles_data["Q1"]-1.5*quantiles_data["IQR"]
quantiles_data["upper_bound"]=quantiles_data["Q3"]+1.5*quantiles_data["IQR"]

df["lower_bound"] = df["category"].map(quantiles_data["lower_bound"])
df["upper_bound"] = df["category"].map(quantiles_data["upper_bound"])

df["is_outlier"] = (
    (df["net_amount"] < df["lower_bound"]) |
    (df["net_amount"] > df["upper_bound"])
)

outliers_before = (
    df.groupby("category")["is_outlier"]
      .sum()
      .rename("outliers_before")
)

df["net_amount_capped"] = df["net_amount"]

df.loc[df["net_amount"] < df["lower_bound"], "net_amount_capped"] = df["lower_bound"]
df.loc[df["net_amount"] > df["upper_bound"], "net_amount_capped"] = df["upper_bound"]

df["is_outlier_after"] = (
    (df["net_amount_capped"] < df["lower_bound"]) |
    (df["net_amount_capped"] > df["upper_bound"])
)

outliers_after = (
    df.groupby("category")["is_outlier_after"]
      .sum()
      .rename("outliers_after")
)

outlier_report = pd.concat(
    [outliers_before, outliers_after],
    axis=1
)

print(outlier_report)
