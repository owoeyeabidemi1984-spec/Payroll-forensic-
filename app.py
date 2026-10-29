import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="Payroll Forensic Audit", page_icon="🛡️", layout="wide")

# --- LOGO / HEADER ---
col1, col2 = st.columns([1, 5])
with col1:
    try:
        st.image("logo.png", width=100)
    except:
        st.markdown("## 🛡️")
with col2:
    st.title("Forensic Payroll Audit Dashboard")
    st.markdown("Detect Ghost Workers, Salary Anomalies & Payroll Fraud")

st.markdown("---")

# --- SIDEBAR ---
st.sidebar.header("Upload Payroll Data")
uploaded_file = st.sidebar.file_uploader("Choose CSV file", type=["csv"])
st.sidebar.info("CSV must contain: StaffID, Name, Department, NetPay, BasicSalary")

# --- MAIN LOGIC ---
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success(f"Loaded {len(df)} records")
    
    st.subheader("1. Payroll Data Preview")
    st.dataframe(df.head(10), use_container_width=True)

    # --- ANALYSIS ---
    # Ensure numeric column exists
    pay_col = None
    for c in ["NetPay", "NETPAY", "Salary", "Amount", "Pay"]:
        if c in df.columns:
           
