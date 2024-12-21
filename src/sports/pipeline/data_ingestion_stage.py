from sports.components.data_ingest import DataIngestion
from sports.config.configuration import ConfigurationManager
from sports.utils.loger import logging
import sys

if __name__ == "__main__":
    """Data Ingestion Stage"""
    try:
        logging.info('Data ingestion stage has started')
        config = ConfigurationManager()
        ingest = DataIngestion(config=config)
        ingest.initiate_data_ingestion()
        logging.info('Data ingestion stage completed')
    except Exception as e:
        logging.error(f"Error in data ingestion stage: {str(e)}")
        sys.exit(1)