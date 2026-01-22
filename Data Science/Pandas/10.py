import pandas as pd

# Load data
df = pd.read_csv("orders.csv")

# Convert date
df["order_date"] = pd.to_datetime(df["order_date"])

# Extract order month
df["order_month"] = df["order_date"].dt.to_period("M")

# Define cohort month (first order month per customer)
df["cohort_month"] = (
    df.groupby("customer_id")["order_month"]
      .transform("min")
)

# Month offset (M0, M1, M2...)
df["month_offset"] = (
    df["order_month"] - df["cohort_month"]
).apply(lambda x: x.n)

# Count active customers per cohort per month
cohort_counts = (
    df.groupby(["cohort_month", "month_offset"])["customer_id"]
      .nunique()
      .reset_index()
)

# Pivot to cohort table
cohort_table = cohort_counts.pivot(
    index="cohort_month",
    columns="month_offset",
    values="customer_id"
)

# Convert to retention percentage
cohort_size = cohort_table[0]
retention = cohort_table.divide(cohort_size, axis=0) * 100

# Rename columns to M0, M1, M2...
retention.columns = ["M" + str(col) for col in retention.columns]

# Final formatting
retention = retention.round(2)

print(retention)
