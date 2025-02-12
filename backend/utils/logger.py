import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),  # Log to a file
        logging.StreamHandler()  # Log to console
    ]
)

def get_logger(name):
    """Get a configured logger."""
    return logging.getLogger(name)
