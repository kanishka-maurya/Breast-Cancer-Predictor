import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion,DataIngestionConfig

try:
    ingestion_config = DataIngestionConfig()
    initiate_ingestion = DataIngestion().initiate_data_ingestion()
    
except Exception as e:
    raise CustomException(e,sys)