import sys
import os
import pandas as pd
from sports.utils.expection import CustomException
from sports.utils.loger import logging
from sports.config.configuration import ConfigurationManager
from sports.utils import save_obj
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix,r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


class ModelTrainer:
    def __init__(self, config = ConfigurationManager()) -> None:
        self.model = config
        



        
    
    def develop_model(self, model_name) -> dict:
        try:
            metrics = {}
            if model_name == 'LogisticRegression':
                 models = LogisticRegression()
            elif model_name == 'DecisionTreeClassifier':
                 models = DecisionTreeClassifier()
            elif model_name == 'RandomForestClassifier':
                 models = RandomForestClassifier()
            elif model_name == 'SVC':
              models = SVC()
            else:
              raise ValueError('invaild model name')
            
            #load the data
            logging.info('loading the data')

            model = self.model.get_data_model_config()
            train_final = pd.read_csv(model.transformed_train_dir)
            test_final = pd.read_csv(model.transformed_test_dir)

            logging.info('data loaded')
            
            X_train = train_final.drop(columns = model.target)
            y_train = train_final[model.target]
            logging.info('train set completed')
            X_test = test_final.drop(columns= model.target, axis=1)
            y_test = test_final[model.target]
            logging.info('test set completed')
            

             #fit the model
            logging.info(f"fitting the model {model_name}")
            models.fit(X_train, y_train)
            logging.info(f"fitting completed on {model_name}")
          
             #predict for train and test data
            model_pred_train = models.predict(X_train)
            model_pred_test = models.predict(X_test)
              
            metrics[model_name] = {
                "train": {
                    "accuracy": accuracy_score(y_train, model_pred_train),
                    "precision": precision_score(y_train, model_pred_train, average='weighted'),
                    "recall": recall_score(y_train, model_pred_train, average='weighted'),
                    "f1": f1_score(y_train, model_pred_train, average='weighted'),
                    "confusion_matrix": confusion_matrix(y_train, model_pred_train),
            },
             "test": {
                "accuracy": accuracy_score(y_test, model_pred_test),
                "precision": precision_score(y_test, model_pred_test, average='weighted'),
                "recall": recall_score(y_test, model_pred_test, average='weighted'),
                "f1": f1_score(y_test, model_pred_test, average='weighted'),
                "confusion_matrix": confusion_matrix(y_test, model_pred_test),
            },
        }
            return metrics
        except Exception as e:
            logging.error(CustomException(e,sys))

    
    def initiate_model_trainer(self) -> dict:
        models = ['LogisticRegression','DecisionTreeClassifier','RandomForestClassifier','SVC']

        model = self.model.get_data_model_config()

        for model_name in models:
            evaulation_metrics = self.develop_model( model_name)
            save_obj(model.model_obj,evaulation_metrics)
        return evaulation_metrics
    



