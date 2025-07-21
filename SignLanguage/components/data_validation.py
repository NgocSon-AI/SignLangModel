import os
import sys
import shutil

from SignLanguage.logger import logging
from SignLanguage.exception import SignException

from SignLanguage.entity.config_entity import DataValidationConfig

from SignLanguage.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact


class DataValidation():
    def __init__(
            self,
            data_ingestion_artifact:DataIngestionArtifact,
            data_validation_config:DataValidationConfig
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise SignException(e, sys)