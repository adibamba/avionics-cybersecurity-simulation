import logging
import os
from logging.handlers import RotatingFileHandler

# Define the log directory and ensure it exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "simulation.log")

class Logger:
    """
    A simple logging wrapper for the simulation.
    Configures logging to both a file (logs/simulation.log) and the console.
    """
    def __init__(self, name="AvionicsSim", log_level=logging.INFO):
        # Get a logger instance
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # Prevent adding handlers multiple times if the class is instantiated more than once
        if not self.logger.handlers:
            # --- File Handler (writes to logs/simulation.log) ---
            # Rotates logs: creates new files when the log file reaches 5MB
            file_handler = RotatingFileHandler(
                LOG_FILE, maxBytes=5*1024*1024, backupCount=2
            )
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)

            # --- Console Handler (prints to the terminal) ---
            console_handler = logging.StreamHandler()
            console_formatter = logging.Formatter('%(levelname)s: %(message)s')
            console_handler.setFormatter(console_formatter)
            self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message, exc_info=False):
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message):
        self.logger.debug(message)

    # A generic log method that can be called from main.py
    def log(self, message, level="info"):
        if level.lower() == "info":
            self.info(message)
        elif level.lower() == "warning":
            self.warning(message)
        elif level.lower() == "error":
            self.error(message)
        elif level.lower() == "debug":
            self.debug(message)
        else:
            self.info(message)

simulation_logger = Logger('simulation_logger')
attack_logger = Logger('attack_logger')
defense_logger = Logger('defense_logger')