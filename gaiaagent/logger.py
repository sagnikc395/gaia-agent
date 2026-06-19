import logging 

def get_logger(name: str) -> logging.Logger:
    # create and configure a logger for the given module or name 
    logging.basicConfig(
        format="%(asctime)s:%(module)s:%(funcName)s:%(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger 