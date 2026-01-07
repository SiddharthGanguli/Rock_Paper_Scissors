from dataclasses import dataclass
from pathlib import Path

@dataclass 
class DataIngestionConfig : 
    root_dir : Path
    source_data :Path
    train_data_path :Path
    test_data_path : Path

@dataclass 
class DataValidationConfig :
    root_dir :Path
    source_data  :Path
    train_data_path :Path
    status_file :Path

