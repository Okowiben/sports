from sports.components.data_validation import DataValiadtion
from sports.config.configuration import ConfigurationManager
from sports.utils.loger import logging
import sys

if __name__ == "__main__":
    """Data Validation Stage"""
    try:
        logging.info('Data validation stage has started')
        config = ConfigurationManager()
        valid = DataValiadtion(config=config)
        valid.validate_all_columns()
        logging.info('Data validation stage completed')
    except Exception as e:
        logging.error(f"Error in data validation stage: {str(e)}")
        sys.exit(1)