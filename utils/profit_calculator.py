def calculate_total_profit(trades):
    """Calculates total profit from a list of trades."""
    total_profit = sum([trade['profit'] for trade in trades])
    return total_profit

def calculate_profit_percentage(initial_balance, final_balance):
    """Calculates profit as a percentage."""
    return ((final_balance - initial_balance) / initial_balance) * 100

def calculate_trade_stats(trades):
    """Calculates statistics like average profit and win rate."""
    wins = [trade for trade in trades if trade['profit'] > 0]
    losses = [trade for trade in trades if trade['profit'] <= 0]
    win_rate = len(wins) / len(trades) if trades else 0
    avg_profit = sum([trade['profit'] for trade in trades]) / len(trades) if trades else 0
    return {
        'win_rate': win_rate,
        'average_profit': avg_profit,
        'num_trades': len(trades)
    }
