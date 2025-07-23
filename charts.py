import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_price_distribution(prices):
    fig, ax = plt.subplots()
    ax.hist(prices, bins=40, color='teal', alpha=0.7)
    ax.axvline(np.median(prices), color='orange', linestyle='--', label='Median')
    ax.axvline(np.min(prices), color='red', linestyle=':', label='Min')
    ax.axvline(np.max(prices), color='green', linestyle=':', label='Max')
    ax.set_title("Simulated Price Distribution")
    ax.set_xlabel("Price")
    ax.set_ylabel("Frequency")
    ax.legend()
    return fig

def plot_percent_change(prices, initial_price):
    percent_changes = (prices - initial_price) / initial_price * 100
    fig, ax = plt.subplots()
    ax.hist(percent_changes, bins=40, color='purple', alpha=0.7)
    ax.axvline(np.median(percent_changes), color='orange', linestyle='--', label='Median')
    ax.axvline(np.min(percent_changes), color='red', linestyle=':', label='Min')
    ax.axvline(np.max(percent_changes), color='green', linestyle=':', label='Max')
    ax.set_title("Percentage Change from Initial Price")
    ax.set_xlabel("Percent Change")
    ax.set_ylabel("Frequency")
    ax.legend()
    return fig

# Sample data to visualize
prices = np.random.normal(100, 15, 1000)
initial_price = 100

st.title("Monte Carlo Simulator Visuals")

# Display first chart
st.subheader("Simulated Price Distribution")
fig1 = plot_price_distribution(prices)
st.pyplot(fig1)

# Display second chart
st.subheader("Percentage Change from Initial Price")
fig2 = plot_percent_change(prices, initial_price)
st.pyplot(fig2)
initial_price = st.sidebar.number_input("Initial Stock Price", min_value=1.0, value=100.0)
volatility = st.sidebar.slider("Volatility", min_value=1.0, max_value=50.0, value=15.0)
num_simulations = st.sidebar.slider("Number of Simulations", min_value=100, max_value=5000, value=1000)

