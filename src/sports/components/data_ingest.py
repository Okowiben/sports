import os
import sys
from sports.utils.expection import CustomException
from sports.utils.loger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sports.config.configuration import DataIngestionConfig
from sports.components.data_transformation import DataTransformation
from sports.components.model import ModelTrainer



class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def get_clean_data(self, df:pd.DataFrame) -> pd.DataFrame:
        try:

          logging.info('data cleaning has started')
          #checking for duplicated rows in the data frame 
          duplicated_rows = df[df.duplicated()]
          
     
  
          #replacing the rows including "as a snack" with their relevant numeric number
          df['servings'] = df['servings'].str.replace(" as a snack", "")
          
  
  
          #converting data type of servings column to integer
          df['servings'] = df['servings'].astype('int')
  
          #replacing the rows with value "High" with True, and null vralues with False
          df['high_traffic'] = np.where(df['high_traffic'] == "High", True, False)
  
          #replacing the 'Breast'with noting 
          df['category'] = df['category'].str.replace(" Breast", "")
  
          #converting data type of category column to category
          df['category']=df['category'].astype('category')
  
          df_clean = df.dropna().reset_index(drop=True)

        except Exception as e:
            logging.error(f"{CustomException(e,sys)}")
        
        logging.info('Data cleaning has ended')

        return df_clean




    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion component')
        try:
            df = pd.read_csv(r'C:\Users\mario\Desktop\sports\notebook\recipe_site_traffic_2212.csv')
            df_clean = self.get_clean_data(df)
            logging.info('read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df_clean.to_csv(self.ingestion_config.raw_data_path,index=False , header=True)

            logging.info('Train test split initiated')
            train_set,test_set = train_test_split(df_clean,test_size=0.2,random_state=40)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)

            logging.info('Ingestion of the data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )

        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        


if __name__ == '__main__':
    try:
       logging.info('<<<<<<<<<******>>>>>>>>')

       logging.info('Pipeline was started')
       ben = DataIngestion()
       train_data,test_data , file_path =ben.initiate_data_ingestion()
   
       DataTransormation = DataTransformation()  
       train_arr, test_arr = DataTransormation.initiate_data_transformation(train_path=train_data,test_path=test_data, target_column='high_traffic',file_path=file_path)


#       moel = ModelTrainer()

#       moel.initiate_model_trainer(train_arr=train_arr ,test_arr=test_arr)
   
       logging.info('Pipeline has ended')
       
       logging.info('<<<<<<<<<******>>>>>>>>')

    except Exception  as e:
       raise CustomException(e,sys)

