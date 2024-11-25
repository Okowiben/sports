import os 
import sys
from sports.utils.expection import CustomException
from sports.utils.loger import logging
from sports.config.configuration import DataModelBuilderConfig
from sports.constants.tans import develop_model

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression




class ModelTrainer:
    def __init__(self) -> None:
        self.model_config = DataModelBuilderConfig()

    def initiate_model_trainer(self, train_arr:np.ndarray , test_arr:np.ndarray):
        try:
            logging.info('Geting the train and test varrables')

            logging.info('done')
        
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
