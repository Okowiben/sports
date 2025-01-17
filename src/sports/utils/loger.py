import logging
import os
import sys

loging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(lineno)s: %(message)s]'

log_dir = 'logs'
log_filepath = os.path.join(log_dir,'running_logs.log')
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= loging_str,
    

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout),
        
    ]
)

