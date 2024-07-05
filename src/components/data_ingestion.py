import os
import sys 
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.exception import CustomException
from src.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig():
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")

class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = read_sql_data()
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)
            
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Data Ingestion completed.")
            
            return (
                self.ingestion_config.raw_data_path,
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) 
        
        except Exception as e:
            raise CustomException(e,sys)
        