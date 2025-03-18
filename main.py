import os
import yaml
from logger import setup_logger
from bots.crypto_trading_bot import CryptoTradingBot
from bots.reinforcement_learning_bot import ReinforcementLearningBot
from utils.profit_calculator import calculate_total_profit
from utils.risk_metrics import calculate_sharpe_ratio
from utils.volatility_analysis import calculate_volatility

# Load configuration
def load_config(config_path="config/config.yaml"):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

# Main function
def main():
    # Load config and initialize logger
    config = load_config()
    logger = setup_logger(log_file=config.get("log_file", "project.log"), 
                          log_level=config.get("log_level", "INFO"))

    logger.info("Starting Statistical Arbitrage Project")

    # Initialize CryptoTradingBot
    trading_bot_config = config.get("trading_bot", {})
    trading_bot = CryptoTradingBot(
        api_key=trading_bot_config.get("api_key"),
        api_secret=trading_bot_config.get("api_secret")
    )
    
    # Fetch market data
    market_data = trading_bot.get_market_data(trading_bot_config.get("trading_pair", "BTC/USD"))
    logger.info(f"Market Data: {market_data}")
    
    # Place a mock order
    order = trading_bot.place_order(
        trading_bot_config.get("trading_pair", "BTC/USD"),
        quantity=trading_bot_config.get("trade_quantity", 0.01),
        order_type="buy"
    )
    logger.info(f"Order Placed: {order}")

    # Initialize ReinforcementLearningBot
    rl_config = config.get("reinforcement_learning", {})
    rl_bot = ReinforcementLearningBot(
        state_size=rl_config.get("state_size", 10),
        action_size=rl_config.get("action_size", 5),
        learning_rate=rl_config.get("learning_rate", 0.001)
    )
    logger.info("Reinforcement Learning Bot Initialized")

    # Simulate RL environment
    rl_bot.simulate_environment()

    # Example: Profit, risk, and volatility analysis
    mock_trades = [{"profit": 100}, {"profit": -50}, {"profit": 200}]
    total_profit = calculate_total_profit(mock_trades)
    logger.info(f"Total Profit: {total_profit}")

    sample_returns = [0.02, 0.03, -0.01, 0.04, -0.02]
    sharpe_ratio = calculate_sharpe_ratio(sample_returns, config.get("risk_free_rate", 0.02))
    logger.info(f"Sharpe Ratio: {sharpe_ratio}")

    sample_prices = [30000, 30500, 31000, 30800, 31500]
    volatility = calculate_volatility(sample_prices)
    logger.info(f"Volatility: {volatility}")

    logger.info("Statistical Arbitrage Project Completed")

if __name__ == "__main__":
    main()
