import sys

from SignLanguage.logger import logging
from SignLanguage.exception import SignException

from SignLanguage.configuration.s3_operations import S3Operation
from SignLanguage.entity.config_entity import ModelPusherConfig
from SignLanguage.entity.artifacts_entity import ModelPusherArtifact, ModelTrainerArtifact


class ModelPusher():
    def __init__(self, model_pusher_config: ModelPusherConfig, model_trainer_artifact:ModelPusherArtifact, s3:S3Operation):
        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifacts = model_trainer_artifact
        self.s3 = s3

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        logging.info("Entered initiate_model_pusher method of ModelPusher class.")
        try:
            self.s3.upload_file(
                self.model_trainer_artifacts.trained_model_file_path,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME
            )
            logging.info("Uploaded best model to s3 bucket.")
            logging.info("Exited initiate model_pusher method of ModelTrainer class.")
            model_pusher_artifact = ModelPusherArtifact(
                bucket_name=self.model_pusher_config.BUCKET_NAME,
                s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH,
            )
            return model_pusher_artifact
        except Exception as e:
            raise SignException(e, sys) from e