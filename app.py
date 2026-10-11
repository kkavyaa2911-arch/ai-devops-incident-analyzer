import time
import logging
import random

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("AI DevOps Incident Analyzer test application started")

while True:
    event = random.choice([
        "normal",
        "normal",
        "normal",
        "database_error",
        "high_cpu"
    ])

    if event == "normal":
        logging.info("Request processed successfully")

    elif event == "database_error":
        logging.error("Database connection failed: connection timeout")
        logging.error("ERROR: Unable to connect to database server")

    elif event == "high_cpu":
        logging.warning("CPU utilization is above 90%")
        logging.error("WARNING: High CPU usage detected")

    time.sleep(10)
