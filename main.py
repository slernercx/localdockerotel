import logging
import json
from datetime import datetime, timezone
import time
import os
from logging.handlers import RotatingFileHandler

# Basic configuration for logging
logger = logging.getLogger('CustomJsonLogger')
logger.setLevel(logging.INFO)

# StreamHandler for stdout
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

# Directory and file for log storage
log_directory = "/var/log/myapp"
log_file = f"{log_directory}/app.log"

# Ensure log directory exists
os.makedirs(log_directory, exist_ok=True)

# RotatingFileHandler for logging to a file with rotation
log_file_max_size = 10 * 1024 * 1024  # Max log file size (e.g., 10 MB)
log_file_backup_count = 3  # Number of backup log files to keep

rotating_file_handler = RotatingFileHandler(
    log_file, maxBytes=log_file_max_size, backupCount=log_file_backup_count
)
logger.addHandler(rotating_file_handler)

# Preamble and logging functions (unchanged)

preamble = "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."

def repeat_preamble_to_size(target_size_kb):
    single_message_size_bytes = len(preamble.encode('utf-8'))
    repetitions_needed = (target_size_kb * 1024) // single_message_size_bytes
    return preamble * repetitions_needed

def log_single_message_with_two_sizes():
    while True:
        log_entry = {
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "severity": "INFO",
            "message": {
                "message1": repeat_preamble_to_size(22),
                "message2": repeat_preamble_to_size(6)
            }
        }
        logger.info(json.dumps(log_entry))
        time.sleep(2)

log_single_message_with_two_sizes()
