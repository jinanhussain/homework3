import os
import logging
from app import App

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def output_env_variables():
    env = os.getenv('ENV')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    log_level = os.getenv('LOG_LEVEL')
    custom_env_var = os.getenv('CUSTOM_ENV_VAR')

    logging.info(f"Environment: {env}")
    logging.info(f"Database User: {db_user}")
    logging.info(f"Database Password: {db_pass}")  
    logging.info(f"Logging Level: {log_level}")
    logging.info(f"Custom Environment Variable: {custom_env_var}")

if __name__ == "__main__":
    logging.info("Starting the app...")

    app = App().start()

    output_env_variables()

    logging.info("App finished execution.")