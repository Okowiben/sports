import os
import sys
from sports.utils.expection import CustomException
from sports.utils.loger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from  sports.config.configuration import ConfigurationManager
from sports.entity import DataValidationConfig



class DataValiadtion:
    def __init__(self , config = ConfigurationManager()):
        self.Validationconfig= config

    def validate_all_columns(self) -> bool:
        try:
            vaild = self.Validationconfig.get_data_validation_config()
            validation_status = None

            data = pd.read_csv(vaild.data_dir)
            all_cols = list(data.columns)

            all_schma = vaild.all_schema.keys()


            for col in all_cols:
                if col not in all_schma:
                    validation_status = False
                    with open(vaild.status_file,'w') as f:
                        f.write(f'vaildation status: {validation_status}')
                else:
                    validation_status = True
                    with open(vaild.status_file, 'w') as f:
                        f.write(f'validation status: {validation_status}')

                return  validation_status
        except Exception as e:
            logging.info(CustomException(e,sys))