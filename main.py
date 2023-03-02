from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity import config_entity 

if __name__ == "__main__":
    try:
        training_pipieline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipieline_config)
        print(data_ingestion_config.to_dic())
        #  get_collection_as_dataframe(database_name = "aps",collection_name = "sensor")
    except Exception as e:
        raise SensorExeption(e,sys)