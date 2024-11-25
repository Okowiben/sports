import sys
import numpy as np
import pandas as pd 
from scipy.stats import  yeojohnson
from sports.utils.expection import CustomException
from sports.utils.loger import logging
from sports.config.configuration import DataTransformationConfig,DataIngestionConfig
from sports.constants.tans import calculate_outlier_limits
from sports.utils import save_obj


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        self.ingestion_config = DataIngestionConfig()


    def get_data_transform(self, df: pd.DataFrame,  name: str ="",
                           transform_numertical: bool = True) -> tuple[pd.DataFrame, list , list]:
        
           logging.info('get data transform has started')

           logging.info('validaing the dataframe')
           if df.empty:
               raise ValueError(f"{name} dataframe is empty")
           
           df_cleaned = df.dropna().reset_index(drop=True)
   
           if df_cleaned.empty:
               raise ValueError(f"{name} dataframe is empty")
           
           logging.info('validatation completed')
           logging.info('geting the num and cat columns')
   
           num_cols = df_cleaned.select_dtypes(include=[np.number]).columns.tolist()
           cat_cols = df_cleaned.select_dtypes(include='object').columns.tolist()
   
           logging.info(f"done, {num_cols} and {cat_cols} goting")
   
           logging.info('appling the the yeojohnson transform to the numeracal col')
           
           if transform_numertical:
               for col in num_cols:
                   try:
                       df_cleaned[col] = yeojohnson(df_cleaned[col])[0]
                   except Exception as e:
                       logging.warning(f'could not apply yeo-johnson transform to column {col}: {str(e)} ')

                       logging.info('get data transform is completed')
                       continue
                       
                
                   return  df_cleaned ,num_cols, cat_cols
                       
                       
            
            
                    
                   
        


        

    def initiate_data_transformation(self , train_path:str ,test_path: str, target_column:str, file_path: str) -> tuple[np.ndarray ,np.ndarray]:
        try:
            logging.info('reading the train and test dataframes')
            train_df = pd.read_csv(train_path)
            test_df =  pd.read_csv(test_path)
            file_df = pd.read_csv(file_path)
            logging.info('reading completed')

            logging.info(f'applying comprehansive transformation on {train_df} and {test_df} ')
            

            train_transform ,num_cols, cat_cols = self.get_data_transform(train_df, 'Training')
            test_transfrom ,_,_ = self.get_data_transform(test_df, 'Test')
            file_transform,_,_ = self.get_data_transform(file_df, 'data')

            logging.info('Performing one-hot encoding')
            train_encoded =  pd.get_dummies(train_transform[cat_cols], drop_first= True)
            test_encoded = pd.get_dummies(test_transfrom[cat_cols], drop_first=True)

            miss_cols = set(train_encoded.columns) - set(test_encoded.columns)
            for col in miss_cols:
                test_encoded = test_encoded[train_encoded.columns]

            train_final = pd.concat([train_transform.drop(columns=cat_cols),train_encoded], axis=1)
            test_final = pd.concat([test_transfrom.drop(columns=cat_cols), test_encoded], axis=1)


            X_train = train_final.drop(columns=target_column)
            y_train = train_final[target_column]
            logging.info('train set completed')
            X_test = test_final.drop(columns=target_column, axis=1)
            y_test = test_final[target_column]
            logging.info('test set completed')


            train_arr = np.column_stack((X_train,y_train))
            test_arr  = np.column_stack((X_test,y_test))

            save_obj(self.data_transformation_config.preprossor_obj_file_path,file_transform)


            logging.info('Data transformation completed successfully')

            return train_arr , test_arr
        except Exception as e:
            logging.error(f'Error in data transformation : {CustomException(e,sys)}')




