import logging

LOGGER_NAME = "biomini"
logger = logging.getLogger(LOGGER_NAME)
logger.addHandler(logging.NullHandler())


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a BioMini namespaced logger without configuring application logging."""
    if not name:
        return logger
    return logging.getLogger(f"{LOGGER_NAME}.{name}")
