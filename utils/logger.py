import logging
import os

def setup_logger(log_file="project.log", log_level=logging.INFO):
    """
    Sets up the logger for the project.

    Parameters:
    - log_file (str): Path to the log file.
    - log_level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
    """
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    log_file_path = os.path.join("logs", log_file)

    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file_path)

    # Set format for the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger(log_level=logging.DEBUG)
    logger.info("Logger is set up successfully!")
    logger.debug("This is a DEBUG message.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")
    logger.critical("This is a CRITICAL message.")
