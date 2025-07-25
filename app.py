import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from simulator import simulate_price
from charts import plot_price_distribution, plot_percent_change
st.set_page_config(page_title="IONQ Monte Carlo Simulator", layout="wide")

# --- UI Controls ---
# ---- UI ----
# ---- UI ----
st.set_page_config(page_title="🔮 IONQ Monte Carlo Simulator", layout="centered")

# Inject responsive CSS styling
st.markdown("""
    <style>
        .sidebar-content {
            padding: 0rem 0.5rem;
        }
        input, select, label {
            font-size: 14px !important;
        }
        .streamlit-expanderHeader {
            font-size: 16px !important;
        }
        .stSlider {
            padding-top: 0.2rem;
            padding-bottom: 0.2rem;
        }
        .stNumberInput input {
            width: 100% !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Title

st.set_page_config(page_title="🔮 IONQ Monte Carlo Simulator", layout="wide")

# Force tighter UI with adjusted max widths and padding
st.markdown("""
    <style>
        .block-container {
            max-width: 700px;
            padding: 1rem;
            margin: auto;
        }
        .sidebar-content {
            padding: 0rem 1rem;
        }
        label, input, .stSlider {
            font-size: 14px !important;
        }
        .streamlit-expanderHeader {
            font-size: 16px !important;
        }
    </style>
    """, unsafe_allow_html=True)


# Sidebar with grouped and collapsed input sections
with st.sidebar:
    st.header("📊 Simulation Parameters")

    with st.expander("💼 Market Assumptions", expanded=True):
        initial_price = st.number_input("Initial Price ($)", value=41.81)
        daily_return = st.number_input("Daily Return", value=0.07 / 252, format="%.6f")
        daily_volatility = st.number_input("Daily Volatility", value=0.02205, format="%.4f")

    with st.expander("📆 Timeframe & Volume", expanded=True):
        time_horizon = st.slider("Time Horizon (Days)", min_value=30, max_value=252, value=126)
        runs = st.slider("Number of Simulations", min_value=100, max_value=10000, step=100, value=1000)

    st.markdown("---")



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
st.markdown("<h4 style='font-size:20px;'>📊 Simulation Results</h4>", unsafe_allow_html=True)
st.pyplot(plot_percent_change(prices, initial_price), use_container_width=True)
st.pyplot(fig, use_container_width=True)
