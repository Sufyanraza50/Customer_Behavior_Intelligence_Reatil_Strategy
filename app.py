from src.cbirs.logger import logging
from src.cbirs.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("Welcome to Customer Behavior Intelligence Retail Strategy Application")


    try:
        raise Exception("Test exception")
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise CustomException(e, sys)
    