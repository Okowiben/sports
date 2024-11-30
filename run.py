from sports.components.data_ingest import DataIngestion
from sports.components.data_transformation import DataTransformation
from sports.components.model import ModelTrainer
from sports.utils.expection import CustomException
from sports.utils.loger import logging
import sys


if __name__ == '__main__':
    try:
       logging.info('<<<<<<<<<******>>>>>>>>')

       logging.info('Pipeline was started')
       ben = DataIngestion()
       train_data,test_data , file_path =ben.initiate_data_ingestion()
   
       DataTransormation = DataTransformation()  
       X_train,y_train,X_test,y_test = DataTransormation.initiate_data_transformation(train_path=train_data,test_path=test_data,target_column='high_traffic',file_path=file_path)

       eveluate = ModelTrainer()
       eve = eveluate.initiate_model_trainer(X_train,y_train,X_test,y_test)
       
    

       


       
   
       logging.info('Pipeline has ended')
       
       logging.info('<<<<<<<<<******>>>>>>>>')

    except Exception  as e:
       raise CustomException(e,sys)


