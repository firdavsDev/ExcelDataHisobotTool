import logging
from functools import wraps


# call logger function in every file it automatically logs all the info in the log file
def set_up_logger(log_file_name="app.log"):
    """
    Set up logger for the app.

    Usage:
    ```
    logger = set_up_logger()
    logger.info("Starting the app...")
    ```
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler = logging.handlers.RotatingFileHandler(
        f"logs/{log_file_name}", maxBytes=1024 * 1024 * 10, backupCount=3
    )
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def log_function(logger):
    """
    Decorator to log function calls.

    Usage:
    ```
    logger = set_up_logger()
    @log_function(logger)
    def my_function():
        pass
    ```
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"Calling {func.__name__}")
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {e}")
                raise

        return wrapper

    return decorator
