import os
import sys

from SignLanguage.logger import logging
from SignLanguage.exception import SignException
from SignLanguage.components.data_ingestion import DataIngestion
from SignLanguage.components.data_validation import DataValidation
from SignLanguage.components.model_trainer import ModelTrainer
from SignLanguage.configuration.s3_operations import S3Operation
from SignLanguage.components.model_pusher import ModelPusher

from SignLanguage.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    ModelTrainerConfig,
    ModelPusherConfig
)

from SignLanguage.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    ModelTrainerArtifact,
    ModelPusherArtifact
)

class TrainPipeline():
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        self.model_pusher_config = ModelPusherConfig()
        self.s3_operations = S3Operation()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the start data_ingestion method of TrainPipeline class.")
            logging.info("Getting the data from URL.")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got data from URL")
            logging.info("Exited the start data_ingestion method of TrainPipeline class.")

            return data_ingestion_artifact
        except Exception as e:
            raise SignException(e, sys)

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            logging.info("Entered the start_data_validation method of TrainPipeline class.")
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Performed the data_validation operation")
            logging.info("Exited the start_data_validation method of TrainPipeline class.")
            
            return data_validation_artifact
        
        except Exception as e:
            raise SignException(e, sys)
    def start_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logging.info("Entered the start_model_trainer method of TrainPipeline class.")
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise SignException(e, sys)
    
    def start_model_pusher(self, model_trainer_artifact: ModelTrainerArtifact, s3:S3Operation):
        try:
            logging.info("Entered the start_model_pusher methods TrainPipeline class.")
            model_pusher = ModelPusher(
                model_pusher_config=self.model_pusher_config,
                model_trainer_artifact=model_trainer_artifact,
                s3=s3
            )
            model_pusher_artifact = model_pusher.initiate_model_pusher()
            return model_pusher_artifact
        except Exception as e:
            raise SignException(e, sys)

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            if data_validation_artifact.validation_status == True:

                model_trainer_artifact = self.start_model_trainer()
                model_pusher_artifact = self.start_model_pusher(model_trainer_artifact=model_trainer_artifact, s3=self.s3_operations)
            else:
                raise Exception("Your data is not in correct format.")
            

        except Exception as e:
            raise SignException(e, sys)