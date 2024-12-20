import os 
import sys
from box.exceptions  import BoxValueError
import yaml
from sports.utils.loger import logging
from sports.utils.expection import CustomException
import json
from typing import Any
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    
    Args:
       path_to_yaml (str): path like input

    Raises:
       valueError: if yaml file is empty

    returns:
      configbox: conffigbox type

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('Ymal file is empty')
    except Exception as e:
        logging.info(CustomException(e,sys))



@ensure_annotations
def create_directories(path_to_directories:list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"create directory at: {path}")


