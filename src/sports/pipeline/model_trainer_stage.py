from sports.components.model import ModelTrainer
from sports.config.configuration import ConfigurationManager
from sports.utils.loger import logging
import sys

if __name__ == "__main__":
    """Model Trainer Stage"""
    try:
        logging.info('Model trainer stage has started')
        config = ConfigurationManager()
        trainer = ModelTrainer(config=config)
        trainer.initiate_model_trainer()
        logging.info('Model trainer stage completed')
    except Exception as e:
        logging.error(f"Error in model trainer stage: {str(e)}")
        sys.exit(1)