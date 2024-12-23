from sports.components.data_transformation import DataTransformation
from sports.config.configuration import ConfigurationManager
from sports.utils.loger import logging
import sys

if __name__ == "__main__":
    """Data Transformation Stage"""
    try:
        logging.info('Data transformation stage has started')
        config = ConfigurationManager()
        trans = DataTransformation(config=config)
        trans.initiate_data_transformation()
        logging.info('Data transformation stage completed')
    except Exception as e:
        logging.error(f"Error in data transformation stage: {str(e)}")
        sys.exit(1)