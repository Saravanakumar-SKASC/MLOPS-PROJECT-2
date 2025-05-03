import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR,f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def get_logger(name):
    import logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger