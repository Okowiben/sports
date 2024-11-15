import os 
from abc import ABC, abstractmethod
import pandas as pd
import os


#implement an abstrat class for data ingestor
class Dataingestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        pass

class ZipFileIngestor(Dataingestor):
    def __init__(self):
        pass

    def ingest(self, file_path: str) -> pd.DataFrame:
                
        return super().ingest(file_path)
    
    