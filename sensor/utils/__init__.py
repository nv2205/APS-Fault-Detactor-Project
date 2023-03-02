import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import sys

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Returns collection as dataframe.
    ================================
    Input:
    Database name
    Collection name
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")

        if "_id" in df.columns:
            df.drop('_id',inplace = True,axis = 1)
        logging.info(f"Rows and Cols: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)