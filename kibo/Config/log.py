import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

Formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
Filehandler = logging.FileHandler("Filelogs.log")
Filehandler.setLevel(logging.INFO)
Filehandler.setFormatter(Formatter)

logger.addHandler(Filehandler)