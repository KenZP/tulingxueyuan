import logging

LOG_FORMAT = "%(asctime)s====%(levelname)s++++++%(message)s"
logging.basicConfig(filename = "ken.log",level=logging.DEBUG,format=LOG_FORMAT)

LOG_FORMAT = "%(asctime)s====%(levelname)s++++++%(message)s"

logging.debug("this is a debug log")
logging.warning("this is a warning log")
logging.log(logging.DEBUG, "this is a debug log")