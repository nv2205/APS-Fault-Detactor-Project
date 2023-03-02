import os,sys
from datetime import datetime
from sensor.exception import SensorException

file_name = "sensor.csv"
train_file_name = "train.csv"
test_file_name = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        self.aftifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")

class DataIngestionConfig:
    def __init__(self,training_pipieline_config:TrainingPipelineConfig):
        try:
            self.database_name = 'aps'
            self.collection_name = 'sensor'
            self.data_ingestion_dir = os.path.join(training_pipieline_config.aftifact_dir,"data_ingestion")
            self.feature_store_dir = os.path.join(self.data_ingestion_dir)
            self.train_file_name = os.path.join(self.data_ingestion_dir,"dataset",train_file_name)
            self.test_file_name = os.path.join(self.data_ingestion_dir,"dataset",test_file_name)
        except Exception as e:
            raise SensorException(e, sys)

    def to_dic(self):
        try:
            pass
        except Exception as e:
            raise SensorExeption(e,sys)

class DataValidationConfig:...

class DataTransformationConfig:...

class ModelTrainingConfig:...

class ModelEvaluationConfig:...

class ModelPusherConfig:...

