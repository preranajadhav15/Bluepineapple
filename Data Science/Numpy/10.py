import numpy as np

# Create 365 days of random daily sales
sales = np.random.randint(50, 200, size=365)

sales[70] = 70000
# Create empty arrays to store rolling results
rolling_7_mean = np.full(365, np.nan)
rolling_30_mean = np.full(365, np.nan)
rolling_30_std  = np.full(365, np.nan)

# Compute rolling statistics using loops
for i in range(365):

    # Rolling 7-day mean
    if i >= 6:
        rolling_7_mean[i] = sales[i-6:i+1].mean()

    # Rolling 30-day mean and std
    if i >= 29:
        rolling_30_mean[i] = sales[i-29:i+1].mean()
        rolling_30_std[i]  = sales[i-29:i+1].std()

# Detect days where sales are unusually high
anomaly_days = np.where(
    sales > (rolling_30_mean + 2 * rolling_30_std)
)[0]

# Output results
print("Anomalous day indices:", anomaly_days)
print("Sales on anomalous days:", sales[anomaly_days])
