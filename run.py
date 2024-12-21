import subprocess
from sports.utils.loger import logging
from sports.utils.expection import CustomException
import sys

if __name__ == "__main__":
    """Main Pipeline Execution"""
    try:
        logging.info('Pipeline execution started')

        # Data Ingestion Stage
        subprocess.run(["python", "src/sports/pipeline/data_ingestion_stage.py"], check=True)

        # Data Validation Stage
        subprocess.run(["python", "src/sports/pipeline/data_validation_stage.py"], check=True)

        # Data Transformation Stage
        subprocess.run(["python", "src/sports/pipeline/data_transformation_stage.py"], check=True)

        # Model Training Stage
        subprocess.run(["python", "src/sports/pipeline/model_trainer_stage.py"], check=True)

        logging.info('Pipeline execution completed successfully')
    except subprocess.CalledProcessError as e:
        logging.error(f"Pipeline execution failed: {str(e)}")
        sys.exit(1)