from sports.components.data_ingest import DataIngestion
from sports.components.data_validation import DataValiadtion
from sports.components.data_transformation import DataTransformation
from sports.utils.expection import CustomException
from sports.utils.loger import logging
from sports.config.configuration import ConfigurationManager
import sys



if __name__ == "__main__":
    try:
        logging.info('Data insgestion has started ')
        config = ConfigurationManager()

        ingest  =  DataIngestion(config=config)
        ingest.initiate_data_ingestion()

        valid = DataValiadtion(config=config)
        valid.validate_all_columns()

        trans = DataTransformation(config=config)
        X_train,y_train,X_test,y_test = trans.initiate_data_transformation()

        
        logging.info('done')
    except Exception as e:
        logging.info(CustomException(e,sys))

        




