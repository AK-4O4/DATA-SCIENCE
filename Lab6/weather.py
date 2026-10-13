import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Messy 15-day weather log (row for 2026-10-09 is duplicated at the end)
raw = {
    "Date": ["2026-10-01", "2026-10-02", "2026-10-03", "2026-10-04", "2026-10-05", "2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11", "2026-10-12", "2026-10-13", "2026-10-14", "2026-10-15", "2026-10-09"],
    "City": ["islamabad", " Islamabad", "ISLAMABAD ", "Islamabad", "islamabad", " ISLAMABAD", "Islamabad ", "islamabad", "Islamabad", " islamabad", "ISLAMABAD", "Islamabad", "islamabad ", " Islamabad", "ISLAMABAD", "Islamabad"],
    "Temperature": ["34C", "35C", "31C", "26C", "25C", "29C", "33C", "36C", "30C", "34C", "28C", "24C", "35C", "29C", "33C", "30C"],
    "Humidity": [40, 38, 55, 80, 85, np.nan, 45, np.nan, 58, 42, 65, 88, np.nan, 62, 48, 58],
    "Condition": ["sunny", " Sunny", "CLOUDY ", " Rainy", "rainy", "cloudy", "SUNNY", "sunny ", "Cloudy", "Sunny", " cloudy", "RAINY", "sunny", "Cloudy ", " SUNNY", "Cloudy"],
}
df = pd.DataFrame(raw)

# (a)
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
df["Temperature"] = df["Temperature"].str.replace("C", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])
df = df.drop_duplicates()
print("Rows after dropping duplicates:", len(df))

median_h = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(median_h)
print("Missing Humidity filled with median:", median_h)

# (b)
df_encoded = pd.get_dummies(df, columns=["Condition"], dtype=int)
print(df_encoded.filter(like="Condition_").head())

# (d)
corr = df["Temperature"].corr(df["Humidity"])
print("Correlation (Temperature, Humidity):", round(corr, 2))

# (e)
counts = df["Condition"].value_counts()
print("Condition counts:")
print(counts)

# (c),(d),(e),(f)
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].plot(df["Date"], df["Temperature"], marker="o", color="steelblue")
axes[0, 0].set_title("Temperature over Date")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (°C)")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].scatter(df["Temperature"], df["Humidity"], color="darkorange", s=60)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (°C)")
axes[0, 1].set_ylabel("Humidity (%)")
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].pie(counts.values, labels=counts.index, autopct="%1.1f%%", startangle=90, colors=["#F2C14E", "#9AA5B1", "#4C78A8"])
axes[1, 0].set_title("Days per Condition")

axes[1, 1].hist(df["Temperature"], bins=5, color="seagreen", edgecolor="white")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (°C)")
axes[1, 1].set_ylabel("Number of Days")

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()
print("Saved weather_dashboard.png")