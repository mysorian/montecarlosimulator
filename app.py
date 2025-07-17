import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from simulator import simulate_price
from charts import plot_price_distribution, plot_percent_change

# --- UI Controls ---
st.title("🔮 IONQ Monte Carlo Simulator")

st.sidebar.header("Simulation Parameters")
initial_price = st.sidebar.number_input("Initial Price ($)", value=41.81)
daily_return = st.sidebar.number_input("Daily Return", value=0.07 / 252)
daily_volatility = st.sidebar.number_input("Daily Volatility", value=0.02205)
time_horizon = st.sidebar.slider("Time Horizon (Days)", min_value=30, max_value=252, value=126)
runs = st.sidebar.slider("Number of Simulations", min_value=100, max_value=10000, step=100, value=1000)

# --- Run Simulation ---
prices = simulate_price(initial_price, daily_return, daily_volatility, time_horizon, runs)

# --- Output ---
st.subheader("📊 Simulation Results")
st.write(f"**Median Price:** ${np.median(prices):.2f}")
st.write(f"**Min Price:** ${np.min(prices):.2f}")
st.write(f"**Max Price:** ${np.max(prices):.2f}")
st.write(f"**Breakout Ratio:** {np.median(prices)/initial_price:.2%}")

st.subheader("📈 Price Distribution")
# st.hist_chart(prices) not available yet
#using matplotlib to have better control
fig, ax = plt.subplots()
ax.hist(prices, bins=40, color='teal', alpha=0.7)
ax.axvline(np.median(prices), color='orange', linestyle='--', label='Median')
ax.axvline(np.min(prices), color='red', linestyle=':', label='Min')
ax.axvline(np.max(prices), color='green', linestyle=':', label='Max')
ax.set_title("Simulated Price Distribution")
ax.set_xlabel("Price")
ax.set_ylabel("Frequency")
ax.legend()
st.pyplot(fig)
# Optional: Show raw data if checkbox enabled
if st.checkbox("Show raw simulation output"):
    st.write(prices)
# plotting charts
# --- 📊 Price Distribution Chart ---
# Visualizing the spread of simulated absolute prices
# st.subheader("📈 Price Distribution")
# st.pyplot(plot_price_distribution(prices))

# --- 📉 Percent Change Chart ---
# Showing performance relative to initial price (% gain or loss)
st.subheader("📉 Percent Change Distribution")
st.pyplot(plot_percent_change(prices, initial_price))
