from utils.common_functions import read_yaml
from src.data_processing import DataProcessing
from src.model_training import ModelTraining
from config.paths_config import *

if __name__ == "__main__":

    data_processing = DataProcessing(ANIME_LIST_CSV,PROCESSED_DIR)
    data_processing.run()

    model_training = ModelTraining(PROCESSED_DIR)
    model_training.train_model()
    