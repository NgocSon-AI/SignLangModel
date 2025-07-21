import os
import sys
import yaml


from SignLanguage.utils.main_utils import read_yaml_file
from SignLanguage.logger import logging
from SignLanguage.exception import SignException

from SignLanguage.entity.config_entity import ModelTrainerConfig
from SignLanguage.entity.artifacts_entity import ModelTrainerArtifact
current_dir = os.path.dirname(os.path.abspath(__file__))
data_yaml_path = os.path.join(current_dir, "../../data/data.yaml")

data_yaml_path = os.path.abspath(data_yaml_path)  # chuẩn hóa tuyệt đối

class ModelTrainer():
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class.")
        try:
            logging.info("Upzipping data.")
            os.system("unzip data.zip")
            os.system("rm data.zip")
            with open(data_yaml_path, "r") as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])
            
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            config['nc'] = int(num_classes)
            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)
            
            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data/data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_result --hyp ../data/my_hyp.yaml --cache")
            os.system("cp yolov5/runs/train/yolov5s_result/weights/best.pt yolov5/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp yolov5/runs/train/yolov5s_result/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")

            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logging.info("Exited initate_model_trainer method of ModelTrainer class.")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)
