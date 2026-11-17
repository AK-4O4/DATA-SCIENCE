import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

homes = pd.read_csv("real_estate.csv")
homes["distance_100m"] = homes["X3 distance to the nearest MRT station"] / 100
X = homes[["distance_100m"]]
y = homes["Y house price of unit area"]
print("Rows:", len(homes))

# (a) fit on all 414 rows
model = LinearRegression()
model.fit(X, y)
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope     : {slope:.4f} price units per 100 m")
print(f"Intercept : {intercept:.4f} price units")

# (b) predict at 500 m (= 5 hundred-metre units), keep the feature name
pred_500 = model.predict(pd.DataFrame({"distance_100m": [5]}))[0]
print(f"Predicted price at 500 m: {pred_500:.2f}")

# (c) plot
xs = pd.DataFrame({"distance_100m": [X["distance_100m"].min(), X["distance_100m"].max()]})
plt.figure(figsize=(8, 5))
plt.scatter(X["distance_100m"], y, alpha=0.5, label="Observations")
plt.plot(xs["distance_100m"], model.predict(xs), color="red", linewidth=2, label="Fitted line")
plt.xlabel("Distance to nearest MRT station (100 m)")
plt.ylabel("House price per unit area (10,000 NTD / ping)")
plt.title("Task 1: Housing price vs distance to MRT")
plt.legend()
plt.tight_layout()
plt.savefig("task1_housing.png", dpi=150)