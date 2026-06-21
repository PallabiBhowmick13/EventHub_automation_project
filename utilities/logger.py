import logging
import os


def get_logger():

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(__name__)

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(
        "logs/automation.log"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

# Console + File Logging Together .Now logs appear: in terminal and in the log file. This is useful for debugging and monitoring the test execution in real-time.

# def get_logger():

#     os.makedirs("logs", exist_ok=True)

#     logger = logging.getLogger()

#     logger.setLevel(logging.DEBUG)

#     formatter = logging.Formatter(
#         "%(asctime)s - %(levelname)s - %(message)s"
#     )

#     file_handler = logging.FileHandler(
#         "logs/automation.log"
#     )

#     console_handler = logging.StreamHandler()

#     file_handler.setFormatter(formatter)
#     console_handler.setFormatter(formatter)

#     logger.addHandler(file_handler)
#     logger.addHandler(console_handler)

#     return logger