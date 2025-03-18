import numpy as np

def calculate_volatility(prices):
    """Calculates historical volatility."""
    log_returns = np.diff(np.log(prices))
    volatility = np.std(log_returns)
    return volatility

def calculate_rolling_volatility(prices, window=30):
    """Calculates rolling volatility over a given window."""
    log_returns = np.diff(np.log(prices))
    rolling_vol = [np.std(log_returns[i:i+window]) for i in range(len(log_returns) - window + 1)]
    return rolling_vol

def analyze_volatility(prices):
    """Analyzes price volatility."""
    vol = calculate_volatility(prices)
    print(f"Historical Volatility: {vol}")
    rolling_vol = calculate_rolling_volatility(prices)
    print(f"Rolling Volatility (last window): {rolling_vol[-1] if rolling_vol else 'N/A'}")
