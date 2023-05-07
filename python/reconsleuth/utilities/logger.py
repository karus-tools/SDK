import logging


def create_logger(name, listen_type) -> logging.Logger:
    if listen_type is None:
        listen_type = logging.NOTSET

    logger = logging.getLogger(name)
    logger.setLevel(listen_type)

    ch = logging.StreamHandler()
    ch.setLevel(listen_type)

    formatter = logging.Formatter("%(asctime)s %(levelname)-10s %(message)s")
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger
