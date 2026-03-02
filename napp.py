import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Student Performance Analytics", layout="wide")

st.title("📊 Student Performance Analytics Dashboard")
st.markdown("Advanced Data Analytics using Pandas, NumPy & Matplotlib")

# -----------------------------
# Create Realistic Dataset
# -----------------------------
np.random.seed(42)
n = 500

df = pd.DataFrame({
    "Student_ID": range(1, n + 1),
    "Age": np.random.randint(17, 23, n),
    "Study_Hours_per_Week": np.random.randint(5, 40, n),
    "Attendance_%": np.random.randint(50, 100, n),
    "Internal_Score": np.random.randint(40, 100, n),
    "Assignment_Score": np.random.randint(40, 100, n),
    "Sleep_Hours": np.random.uniform(4, 9, n).round(1),
    "Internet_Usage_Hours": np.random.uniform(1, 8, n).round(1)
})

# More realistic Final Score calculation
df["Final_Score"] = (
    df["Internal_Score"] * 0.4 +
    df["Assignment_Score"] * 0.3 +
    df["Attendance_%"] * 0.2 +
    df["Study_Hours_per_Week"] * 0.1
).round(2)

# Ensure score capped at 100
df["Final_Score"] = df["Final_Score"].clip(0, 100)

# -----------------------------
# Grade Assignment (FIXED)
# -----------------------------
df["Grade"] = pd.cut(
    df["Final_Score"],
    bins=[0, 40, 50, 60, 75, 90, 100],
    labels=["F", "E", "D", "C", "B", "A"]
)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔎 Filter Students")

min_score = st.sidebar.slider("Minimum Final Score", 0, 100, 0)
selected_grade = st.sidebar.multiselect(
    "Select Grade",
    options=df["Grade"].unique(),
    default=df["Grade"].unique()
)

filtered_df = df[
    (df["Final_Score"] >= min_score) &
    (df["Grade"].isin(selected_grade))
]

# -----------------------------
# KPI Section
# -----------------------------
st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(filtered_df))
col2.metric("Average Score", round(filtered_df["Final_Score"].mean(), 2))
col3.metric("Highest Score", round(filtered_df["Final_Score"].max(), 2))
col4.metric("Lowest Score", round(filtered_df["Final_Score"].min(), 2))

# -----------------------------
# Show Data
# -----------------------------
st.subheader("📄 Student Dataset")
st.dataframe(filtered_df, use_container_width=True)

# -----------------------------
# Visualization Section
# -----------------------------
st.subheader("📊 Visual Analytics")

# 1️⃣ Score Distribution
fig1, ax1 = plt.subplots()
ax1.hist(filtered_df["Final_Score"], bins=20)
ax1.set_title("Final Score Distribution")
ax1.set_xlabel("Final Score")
ax1.set_ylabel("Number of Students")
st.pyplot(fig1)

# 2️⃣ Study Hours vs Final Score
fig2, ax2 = plt.subplots()
ax2.scatter(filtered_df["Study_Hours_per_Week"], filtered_df["Final_Score"])
ax2.set_title("Study Hours vs Final Score")
ax2.set_xlabel("Study Hours per Week")
ax2.set_ylabel("Final Score")
st.pyplot(fig2)

# 3️⃣ Grade Distribution
fig3, ax3 = plt.subplots()
filtered_df["Grade"].value_counts().sort_index().plot(kind="bar", ax=ax3)
ax3.set_title("Grade Distribution")
ax3.set_xlabel("Grade")
ax3.set_ylabel("Count")
st.pyplot(fig3)

# 4️⃣ Correlation Heatmap
st.subheader("📈 Correlation Heatmap")

numeric_cols = filtered_df.select_dtypes(include=np.number)
corr = numeric_cols.corr()

fig4, ax4 = plt.subplots()
cax = ax4.matshow(corr)
fig4.colorbar(cax)
ax4.set_xticks(range(len(corr.columns)))
ax4.set_yticks(range(len(corr.columns)))
ax4.set_xticklabels(corr.columns, rotation=90)
ax4.set_yticklabels(corr.columns)
st.pyplot(fig4)

# -----------------------------
# Download Option
# -----------------------------
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_student_data.csv",
    mime="text/csv"
)

st.success("✅ Dashboard Loaded Successfully!")