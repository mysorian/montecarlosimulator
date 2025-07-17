import numpy as np

def simulate_price(initial_price, daily_return, daily_volatility, time_horizon, runs):
    # Generate daily returns: normally distributed with drift and volatility
    daily_returns = np.random.normal(daily_return, daily_volatility, (runs, time_horizon))
    # Simulate cumulative return and final price
    cumulative_returns = np.cumsum(daily_returns, axis=1)
    price_paths = initial_price * np.exp(cumulative_returns)
    final_prices = price_paths[:, -1]
    return final_prices
if __name__ == "__main__":
    prices = simulate_price(
        initial_price=41.81,
        daily_return=0.07 / 252,
        daily_volatility=0.02205,
        time_horizon=126,
        runs=10
    )
    print("Sample Simulated Prices:")
    print(prices)
