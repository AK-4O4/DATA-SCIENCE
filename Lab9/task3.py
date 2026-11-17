import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import GridSearchCV, KFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

concrete = pd.read_csv("concrete_strength.csv").drop_duplicates()
target = "Concrete compressive strength"
X = concrete.drop(columns=target)
y = concrete[target]

# (a) hold out 20%, baseline CV on the training rows
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
print("Training rows:", len(X_train), "| Test rows:", len(X_test))

folds = KFold(n_splits=5, shuffle=True, random_state=42)
scoring = "neg_root_mean_squared_error"
baseline_rmse = -cross_val_score(LinearRegression(), X_train, y_train, cv=folds, scoring=scoring)
print(f"Baseline linear mean CV RMSE: {baseline_rmse.mean():.2f} MPa")

# (b) polynomial + scaling + Ridge, tuned on the same folds
pipe = Pipeline([
    ("poly", PolynomialFeatures(include_bias=False)),
    ("scale", StandardScaler()),
    ("ridge", Ridge()),
])
grid = {"poly__degree": [1, 2, 3], "ridge__alpha": [0.01, 0.1, 1, 10, 100]}
search = GridSearchCV(pipe, grid, cv=folds, scoring=scoring, refit=True)
search.fit(X_train, y_train)

res = pd.DataFrame(search.cv_results_).sort_values("rank_test_score").head(3)
print("\nTop 3 settings:")
for _, r in res.iterrows():
    print(f"  rank {int(r['rank_test_score'])}: {r['params']}  mean CV RMSE = {-r['mean_test_score']:.2f} MPa")

# (c) test performance of the refitted winner
pred = search.predict(X_test)
test_rmse = np.sqrt(mean_squared_error(y_test, pred))
test_mae = mean_absolute_error(y_test, pred)
print(f"\nBest parameters: {search.best_params_}")
print(f"Tuned mean CV RMSE: {-search.best_score_:.2f} MPa")
print(f"Test RMSE: {test_rmse:.2f} MPa")
print(f"Test MAE : {test_mae:.2f} MPa")

lo, hi = min(y_test.min(), pred.min()), max(y_test.max(), pred.max())
plt.figure(figsize=(6, 6))
plt.scatter(y_test, pred, alpha=0.6, label="Test samples")
plt.plot([lo, hi], [lo, hi], "r--", label="y = x")
plt.xlabel("Actual strength (MPa)")
plt.ylabel("Predicted strength (MPa)")
plt.title("Task 3: Actual vs predicted concrete strength")
plt.legend()
plt.tight_layout()
plt.savefig("task3_concrete.png", dpi=150)

# (d) comparison
print(f"\nBaseline CV RMSE {baseline_rmse.mean():.2f} -> tuned CV RMSE {-search.best_score_:.2f} MPa")