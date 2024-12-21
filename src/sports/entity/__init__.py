from dataclasses import dataclass
from pathlib import Path
from ensure import ensure_annotations

@dataclass(frozen=True)
class DataIngestionConfig:
   root_dir: Path
   source_dir: str
   cleaned_dir: Path
   train_dir: Path
   test_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
   root_dir: Path
   data_dir: str
   status_file: Path
   all_schema: str


@dataclass(frozen=True)
class DataTransformationConfig:
   root_dir: Path
   data_dir: Path
   train_dir: Path
   test_dir: Path
   transform_dir: Path
   transformed_train_dir: Path
   transformed_test_dir: Path
   target: str

@dataclass(frozen=True)
class DataModelConfig:
   root_dir: Path
   transformed_train_dir: Path
   transformed_test_dir: Path
   target: str
   model_obj: Path
 
   



   