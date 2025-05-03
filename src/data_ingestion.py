import os
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_names = self.config["bucket_file_names"]
        
        os.makedirs(RAW_DIR,exist_ok=True)

        logger.info("Data Ingestion Initiated")

    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file_name in self.file_names:
                file_path = os.path.join(RAW_DIR, file_name)
                blob = bucket.blob(file_name)

                if file_name == "animelist.csv":
                    logger.info("Streaming only first 5 million rows of animelist.csv")
                    with blob.open("rt") as f:
                        chunks = pd.read_csv(f, chunksize=100_000)
                        result = []
                        total = 0
                        for chunk in chunks:
                            result.append(chunk)
                            total += len(chunk)
                            if total >= 5_000_000:
                                break
                        pd.concat(result).iloc[:5_000_000].to_csv(file_path, index=False)
                        logger.info("Saved 5M rows of animelist.csv")
                else:
                    blob.download_to_filename(file_path)
                    logger.info(f"Downloaded {file_name} from GCP bucket")

        except Exception as e:
            logger.error("Error while downloading data from GCP")
            raise CustomException(f"Failed to download csv from GCP bucket: {str(e)}")

    def run(self):
        try:
            
            self.download_csv_from_gcp()
            logger.info("Data Ingestion Completed")
        except Exception as e:
            logger.error("Error while running Data Ingestion")
            raise CustomException(f"Failed to download csv from GCP bucket: {str(e)}")
        
        finally:
            logger.info("Data Ingestion Completed")

if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()