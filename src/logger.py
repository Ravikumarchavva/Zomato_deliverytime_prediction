import logging
import sys
sys.path.append("..")
from config.configs import ROOT_DIR

SRC_DIR = ROOT_DIR / "src"

# Path to the log file
LOG_DIR = SRC_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)  # Ensure the logs directory exists
LOG_FILE = LOG_DIR / "zomato_project.log"

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG for detailed logs; change to INFO in production
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Log to console as well
    ]
)

# Create a logger instance
logger = logging.getLogger("ZomatoProject")