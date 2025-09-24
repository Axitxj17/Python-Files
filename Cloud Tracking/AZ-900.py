import pandas as pd
import random
import datetime

resources = ["VM1", "VM2", "WebApp1"]
metrics = ["CPU", "Memory", "NetworkIn", "NetworkOut"]
data = []

for hour in range(24):  # simulate 24 hours
    timestamp = datetime.datetime.now() - datetime.timedelta(hours=24-hour)
    for res in resources:
        for metric in metrics:
            value = round(random.uniform(10, 90), 2)
            data.append({
                "Resource": res,
                "Metric": metric,
                "Time": timestamp,
                "Value": value
            })

df = pd.DataFrame(data)
df.to_csv("simulated_metrics.csv", index=False)
print(df.head())

# Cost per hour per resource
cost_per_hour = {"VM1": 0.05, "VM2": 0.05, "WebApp1": 0.03}

# Calculate cost based on metric (simple simulation)
df["Cost"] = df.apply(lambda row: cost_per_hour[row["Resource"]], axis=1)

# Aggregate total daily cost
daily_cost = df.groupby("Resource")["Cost"].sum().reset_index()
daily_cost.to_csv("daily_cost.csv", index=False)
print(daily_cost)

df["Alert"] = df["Value"].apply(lambda x: "High CPU" if x>80 else "")
alerts = df[df["Alert"]!=""]
alerts.to_csv("alerts.csv", index=False)
print(alerts)


