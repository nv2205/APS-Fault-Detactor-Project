import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

class EnvironmentVariable:
    mongo_db_url:str = os.getenv("mongo_db_url")

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)