import os
import sys
import zipfile
import urllib
import urllib.request

from SignLanguage.logger import logging
from SignLanguage.exception import SignException

from SignLanguage.entity.config_entity import DataIngestionConfig
from SignLanguage.entity.artifacts_entity import DataIngestionArtifact

class DataIngestion():
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config      # khoi tao data_ingestion config = class DataIngestionConfig()
        except Exception as e:
            raise SignException(e, sys)
    def download_data(self) -> str:
        """
        Fetch data from the url
        """
        try:
            dataset_url = self.data_ingestion_config.data_download_url                      # Lay ra duong dan data_download_url trong data_ingestion_config
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir                # Lấy đường dẫn thư mục để chứa file zip đã tải về.
            os.makedirs(zip_download_dir, exist_ok=True)                                    # Tạo thư mục lưu file zip nếu chưa tồn tại. Nếu thư mục đã tồn tại thì không báo lỗi (nhờ exist_ok=True).
            data_file_name = os.path.basename(dataset_url)                                  # Lấy tên file zip từ URL.
            zip_file_path = os.path.join(zip_download_dir, data_file_name)                  # Nối đường dẫn thư mục với tên file để ra đường dẫn đầy đủ file zip sẽ lưu:
            logging.info(f"Downloaded data from {dataset_url} info file {zip_file_path}")   # Ghi log thông báo bắt đầu download.
            urllib.request.urlretrieve(dataset_url, zip_file_path)                          # Thực hiện download file zip từ URL về máy. Lưu trực tiếp vào đường dẫn zip_file_path ở trên.
            logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")   # Ghi log thông báo đã download xong.

            return zip_file_path
        except SignException as e:
            raise SignException(e, sys)
        
    def extract_zip_file(self, zip_file_path:str) -> str:
        """
        Zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path                 # Lấy đường dẫn thư mục feature_store, nơi sẽ giải nén dữ liệu vào.
            os.makedirs(feature_store_path, exist_ok=True)                                          # Tạo thư mục feature_store nếu chưa có.
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:                                    # Mở file zip vừa tải về bằng zipfile.ZipFile.
                zip_ref.extractall(feature_store_path)                                              # Giải nén toàn bộ nội dung file zip vào thư mục feature_store_path.
            logging.info(f"Extracting zip file: {zip_file_path} into dir: {feature_store_path}")    # Ghi log quá trình giải nén
            return feature_store_path
        except Exception as e:
            raise SignException(e, sys)
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of Data Ingestion class.")
        try:
            zip_file_path = self.download_data()                        # Goi ham download data
            feature_store_path = self.extract_zip_file(zip_file_path)   # Giai nen data

            data_ingestion_artifact = DataIngestionArtifact(            # Tạo một DataIngestionArtifact để đóng gói kết quả của bước ingestion
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )
            logging.info("Exited initiate_data_ingestion method of Data Ingestion class.")
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact
        except Exception as e:
            raise SignException(e, sys)
        