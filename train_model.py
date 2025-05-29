import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

# データ読み込み
df = pd.read_csv("sample_sales_data_2.csv", parse_dates=["Date"])

# カテゴリ変数に変換
df["Date"] = df["Date"].astype("category")
df["Month"] = df["Month"].astype("category")
df["Weather"] = df["Weather"].astype("category")

# 特徴量と目的変数に分割
X = df[["Date", "Month", "Ad Spend (10K yen)", "Weather", "Temperature (C)"]]
y = df["Sales (10K yen)"]

# OneHotEncoding
X_encoded = pd.get_dummies(X)

# 学習用とテスト用に分割
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# モデル訓練
model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# 保存（モデルと列構成）
with open("sales_model.pkl", "wb") as f:
    pickle.dump({"model": model, "columns": X_encoded.columns.tolist()}, f)

print("Model training and saving completed.")
