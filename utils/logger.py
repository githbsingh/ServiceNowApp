import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    filemode="w"   # overwrite every run
)

logger = logging.getLogger(__name__)