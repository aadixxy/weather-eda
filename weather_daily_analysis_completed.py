import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the daily weather dataset
df = pd.read_csv("weather.csv")

# The supplied CSV has no Date column, so use row order as the daily index.
df["Day"] = range(1, len(df) + 1)

# 2. Explore the data
print("First five rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nSummary statistics:")
print(df[["MinTemp", "MaxTemp", "Rainfall", "Humidity9am", "Humidity3pm"]].describe())

# 3. Daily temperature trend
plt.figure(figsize=(11, 5))
plt.plot(df["Day"], df["MinTemp"], label="Minimum temperature")
plt.plot(df["Day"], df["MaxTemp"], label="Maximum temperature")
plt.xlabel("Day (dataset order)")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Trend")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Daily rainfall trend
plt.figure(figsize=(11, 4.5))
plt.bar(df["Day"], df["Rainfall"], width=1.0)
plt.xlabel("Day (dataset order)")
plt.ylabel("Rainfall (mm)")
plt.title("Daily Rainfall")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# 5. Daily humidity trend
plt.figure(figsize=(11, 5))
plt.plot(df["Day"], df["Humidity9am"], label="Humidity 9am")
plt.plot(df["Day"], df["Humidity3pm"], label="Humidity 3pm")
plt.xlabel("Day (dataset order)")
plt.ylabel("Humidity (%)")
plt.title("Daily Humidity Trend")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Rainfall and humidity relationship
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Humidity3pm", y="Rainfall")
plt.xlabel("Humidity at 3pm (%)")
plt.ylabel("Rainfall (mm)")
plt.title("Rainfall vs 3pm Humidity")
plt.tight_layout()
plt.show()

# 7. Key summaries
rain_days = (df["Rainfall"] > 0).sum()
print(f"\nNumber of days: {len(df)}")
print(f"Rainy days: {rain_days}")
print(f"Dry days: {len(df) - rain_days}")
print(f"Rainy-day percentage: {rain_days / len(df) * 100:.2f}%")
print(f"Average minimum temperature: {df['MinTemp'].mean():.2f} °C")
print(f"Average maximum temperature: {df['MaxTemp'].mean():.2f} °C")
print(f"Average rainfall: {df['Rainfall'].mean():.2f} mm")
print(f"Average humidity at 9am: {df['Humidity9am'].mean():.2f}%")
print(f"Average humidity at 3pm: {df['Humidity3pm'].mean():.2f}%")
print(f"Highest maximum temperature: {df['MaxTemp'].max():.2f} °C")
print(f"Lowest minimum temperature: {df['MinTemp'].min():.2f} °C")
print(f"Highest daily rainfall: {df['Rainfall'].max():.2f} mm")

# Note: The original dataset has no Date column, so calendar-month
# analysis cannot be performed without adding a trusted date source.
