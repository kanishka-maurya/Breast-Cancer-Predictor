# This file contains common functionality.

import os
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from dotenv import load_dotenv
import pymysql
import pandas as pd

load_dotenv()


def read_sql_data():
    
    logging.info("Reading MySQL data.")
    
    try:
      my_db = pymysql.connect(
        host = os.getenv("host"),
        user = os.getenv("user"),
        password = os.getenv("password"),
        db = os.getenv("db")
      )
      
      logging.info("Connection Established.",my_db)
      
      df = pd.read_sql_query("SELECT * FROM data",my_db)
      return df
    
    except Exception as e:
      raise CustomException(e,sys)