# streamlit_app.py
import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import streamlit as st
import numpy as np
from bs_model import black_scholes, bs_greeks

st.title("Black-Scholes Option Pricing App")

# Sidebar inputs
st.sidebar.header("Input Parameters")
S = st.sidebar.slider("Spot Price (S)", 50, 200, 100)
K = st.sidebar.slider("Strike Price (K)", 50, 200, 100)
T = st.sidebar.slider("Time to Expiry (T in years)", 1, 365, 30) / 365
r = st.sidebar.slider("Risk-Free Rate (r)", 0.0, 0.1, 0.03)
sigma = st.sidebar.slider("Volatility (σ)", 0.01, 1.0, 0.2)
q = st.sidebar.slider("Dividend Yield (q)", 0.0, 0.1, 0.0)
option_type = st.sidebar.selectbox("Option Type", ['call', 'put'])

# Pricing
price = black_scholes(S, K, T, r, sigma, option_type, q=q)
delta, gamma, vega, theta, rho = bs_greeks(S, K, T, r, sigma, option_type, q=q)

#Output
st.subheader("Option Price")
st.markdown(f"<span style='font-size: 1.5em;'>${price:.2f}</span>", unsafe_allow_html=True)

st.subheader("Greeks")
st.write(f"<span style='color: green;'>**Delta:**</span> {delta:.4f}", unsafe_allow_html=True)
st.write(f"<span style='color: green;'>**Gamma:**</span> {gamma:.4f}", unsafe_allow_html=True)
st.write(f"<span style='color: green;'>**Vega:**</span> {vega:.2f}", unsafe_allow_html=True)
st.write(f"<span style='color: green;'>**Theta:**</span> {theta:.4f}", unsafe_allow_html=True)
st.write(f"<span style='color: green;'>**Rho:**</span> {rho:.4f}", unsafe_allow_html=True)