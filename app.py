import streamlit as st
import pandas as pd
import pickle

# モデル読み込み
with open("sales_model.pkl", "rb") as f:
    data = pickle.load(f)

model = data["model"]
columns = data["columns"]

st.set_page_config(page_title="Sales Forecast Simulator", layout="centered")

st.title("🔮 Sales Forecast Simulator")

# 入力フォーム
month = st.selectbox("📅 Month", [str(i) for i in range(1, 13)])
day = st.selectbox("📆 Date", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
ad_spend = st.number_input("📢 Ad Spend (10K yen)", value=1000)
weather = st.selectbox("⛅ Weather", ["Sunny", "Rainy", "Cloudy"])
temperature = st.number_input("🌡️ Temperature (C)", value=25)

if st.button("Predict Sales"):
    # 入力をDataFrame化
    input_df = pd.DataFrame([{
        "Date": day,
        "Month": month,
        "Ad Spend (10K yen)": ad_spend,
        "Weather": weather,
        "Temperature (C)": temperature
    }])

    # One-hot encodingと列整形
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    # 予測
    pred = model.predict(input_encoded)[0]
    st.success(f"💰 Predicted Sales: ¥{pred:,.2f}")