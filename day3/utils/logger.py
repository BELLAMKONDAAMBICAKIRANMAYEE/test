import logging
import os

os.makedirs("logs",exist_ok=True)

def get_logger(name:str) -> logging.Logger:
    logger=logging.getLogger(name)
    if logger.handlers:
        return logger

    formatter=logging.Formater("%(ascetime)s | %(levelname)s | %(name)s | %(message)s",datefmt="%Y-%m-%d %H:%H:%S")

    console=logging.StreamHandler()
    console.setFormatter(formatter)

    file_handler=logging.FileHandler("logs/app.log")

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger
