import os
from sports.utils.expection import CustomException
import sys
from dataclasses import dataclass
from sports.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from sports.utils.common import read_yaml,create_directories
from sports.entity import DataIngestionConfig ,DataValidationConfig, DataTransformationConfig
from ensure import ensure_annotations


class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.data_root])

    


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_dir= config.source_dir,
            cleaned_dir = config.cleaned_dir,
            train_dir=config.train_dir,
            test_dir= config.test_dir

        )

        return data_ingestion_config
    
    def get_data_validation_config(self)-> DataValidationConfig:
        try:
            confi = self.config.data_validation
            schema = self.schema.Columns

            create_directories([confi.root_dir])

            data_validation_config = DataValidationConfig(
               root_dir= confi.data_dir,
               data_dir=  confi.data_dir,
               status_file=  confi.status_file,
               all_schema= schema,
        
            
        )
        except Exception as e:
           raise CustomException(e, sys)
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_tranasformation

        create_directories([config.root_dir])   


        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_dir = config.data_dir,
            train_dir= config.train_dir,
            test_dir= config.test_dir,
            transform_dir= config.transform_dir,
            target= config.target
        )    
        return data_transformation_config
