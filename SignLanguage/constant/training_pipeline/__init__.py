import os

ARTIFACT_DIR: str = "artifacts"

"""
    Data ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://github.com/NgocSon-AI/data/raw/refs/heads/main/data.zip"



"""
    Data Validation related constant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "test", "data.yaml", "my_hyp.yaml"]


"""
    MODEL TRAINER related constant start with MODEL_TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME:str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME:str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16


"""
    MODEL PUSHER related constant start with MODEL_PUSHER VAR NAME.
"""

BUCKET_NAME = "ngocson-sign-lang-2025"

S3_MODEL_NAME = "best.pt"
