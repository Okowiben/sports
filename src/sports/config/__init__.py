import os
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str=os.path.join('data', 'raw.csv')
    test_data_path: str=os.path.join('data', 'test.csv')
    train_data_path: str=os.path.join('data', 'train.csv')

    
    

@dataclass 
class DataTransformationConfig:
    preprossor_obj_file_path = os.path.join('data','preprocessor.pkl')


@dataclass
class DataModelBuilderConfig:
    model_path = os.path.join('data', 'model.pkl')

    
    
    