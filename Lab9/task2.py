import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

yachts = pd.read_csv("yacht_hydrodynamics.data", sep=r"\s+", header=None)
X = yachts[[5]]   # Froude number
y = yachts[6]     # Residuary resistance per unit displacement weight
print("Rows:", len(yachts))

# (a) models
linear_model = LinearRegression()
quadratic_model = Pipeline([
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("linear", LinearRegression()),
])

# (b) same five shuffled folds for both models
folds = KFold(n_splits=5, shuffle=True, random_state=42)
scoring = "neg_root_mean_squared_error"
linear_rmse = -cross_val_score(linear_model, X, y, cv=folds, scoring=scoring)
quadratic_rmse = -cross_val_score(quadratic_model, X, y, cv=folds, scoring=scoring)

print("Linear   fold RMSEs:", linear_rmse.round(2), "mean:", linear_rmse.mean().round(2))
print("Quadratic fold RMSEs:", quadratic_rmse.round(2), "mean:", quadratic_rmse.mean().round(2))

# (c) choose the better model
best = "Quadratic" if quadratic_rmse.mean() < linear_rmse.mean() else "Linear"
print("Better model by mean RMSE:", best)