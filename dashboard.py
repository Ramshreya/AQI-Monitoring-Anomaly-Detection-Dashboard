import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import streamlit as st

st.title("Hyderabad AQI Monitoring & Anomaly Detection Dashboard")

df = pd.read_csv("hyderabad_aqi_3months.csv")
df["datetime"] = pd.to_datetime(df["datetime"])
df = df.sort_values("datetime")

df["z_score"] = stats.zscore(df["aqi"])
df["anomaly"] = df["z_score"].apply(lambda x: 1 if abs(x) > 3 else 0)

st.subheader("AQI Trend with Anomalies")

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(df["datetime"], df["aqi"], label="AQI Trend")
anomalies = df[df["anomaly"] == 1]
ax.scatter(anomalies["datetime"], anomalies["aqi"], color="red", label="Anomaly")
ax.set_xlabel("Time")
ax.set_ylabel("AQI")
ax.legend()

st.pyplot(fig)
