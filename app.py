from SignLanguage.logger import logging
from SignLanguage.exception import SignException

import sys


logging.info("Welcome to the My Project!!!")

from SignLanguage.pipeline.training_pipeline import TrainPipeline


obj = TrainPipeline()
obj.run_pipeline()