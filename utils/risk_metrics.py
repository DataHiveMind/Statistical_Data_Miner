import numpy as np

def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
    """Calculates the Sharpe Ratio."""
    excess_returns = np.mean(returns) - risk_free_rate
    std_dev = np.std(returns)
    return excess_returns / std_dev if std_dev != 0 else 0

def calculate_drawdown(returns):
    """Calculates the maximum drawdown."""
    cumulative_returns = np.cumsum(returns)
    peak = np.maximum.accumulate(cumulative_returns)
    drawdown = cumulative_returns - peak
    max_drawdown = np.min(drawdown)
    return max_drawdown

def calculate_value_at_risk(returns, confidence_level=0.95):
    """Calculates Value at Risk (VaR)."""
    sorted_returns = np.sort(returns)
    index = int((1 - confidence_level) * len(sorted_returns))
    return sorted_returns[index]
