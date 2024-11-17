import logging
import os

def configure_logging(log_file="logs/app.log"):
    # Ensure the logs directory exists
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # File logging configuration
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Console logging configuration
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(asctime)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    # Root logger
    logger = logging.getLogger()
    logger.addHandler(console_handler)

    return logger