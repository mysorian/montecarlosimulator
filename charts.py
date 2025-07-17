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
