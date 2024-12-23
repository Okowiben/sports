import os
import sys
from sports.utils.expection import CustomException
from sports.utils.loger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from  sports.config.configuration import ConfigurationManager



class DataIngestion:
    def __init__(self, config = ConfigurationManager()):
        self.ingestion_config = config

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
        """
        this funtion
        """
        logging.info('Entered the data ingestion component')
        try:
            ing = self.ingestion_config.get_data_ingestion_config()
            df = pd.read_csv(ing.source_dir)
            df_clean = self.get_clean_data(df)
            logging.info('read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(ing.root_dir), exist_ok=True)

            df_clean.to_csv(ing.cleaned_dir,index=False , header=True)

            logging.info('Train test split initiated')
            train_set,test_set = train_test_split(df_clean,test_size=0.2,random_state=40)

            train_set.to_csv(ing.train_dir, index=False,header=True)
            test_set.to_csv(ing.test_dir, index=False,header=True)

            logging.info('Ingestion of the data is completed')

            return (
                ing.train_dir,
                ing.test_dir,
                ing.root_dir
            )

            

        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        
        

def main():
    data_ingest = DataIngestion()
    data_ingest.initiate_data_ingestion()