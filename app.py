from SignLanguage.logger import logging
from SignLanguage.exception import SignException

import sys


logging.info("Welcome to the My Project!!!")

try:
    a = 4/'9'
except Exception as e:
    raise SignException(e, sys) from e