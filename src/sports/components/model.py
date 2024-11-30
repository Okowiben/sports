import sys
import os
import pandas as pd
from sports.utils.expection import CustomException
from sports.utils.loger import logging
from sports.config.configuration import DataModelBuilderConfig
from sports.utils import save_obj
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix,r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


class ModelTrainer:
    def __init__(self) -> None:
        self.model_path = DataModelBuilderConfig() 
        logging.info('Model training has started')



        
    
    def develop_model(self, X_train,y_train,X_test,y_test, model_name) -> dict:
        try:
            metrics = {}
            if model_name == 'LogisticRegression':
                 model = LogisticRegression()
            elif model_name == 'DecisionTreeClassifier':
                 model = DecisionTreeClassifier()
            elif model_name == 'RandomForestClassifier':
                 model = RandomForestClassifier()
            elif model_name == 'SVC':
              model = SVC()
            else:
              raise ValueError('invaild model name')
             #fit the model
            logging.info(f"fitting the model {model_name}")
            model.fit(X_train, y_train)
            logging.info(f"fitting completed on {model_name}")
          
             #predict for train and test data
            model_pred_train = model.predict(X_train)
            model_pred_test = model.predict(X_test)
              
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

    
    def initiate_model_trainer(self,X_train,y_train,X_test,y_test):
        models = ['LogisticRegression','DecisionTreeClassifier','RandomForestClassifier','SVC']

        for model_name in models:
            evaulation_metrics = self.develop_model(X_train,y_train,X_test,y_test, model_name)
            save_obj(self.model_path.model_path,evaulation_metrics)
        return evaulation_metrics