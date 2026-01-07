import os
from pathlib import Path
import yaml

from ml_ops.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig
)


class ConfigurationManager : 
    def __init__(self,config_filepath : Path):
        self.config_filepath=self._read_yaml(config_filepath)

    def _read_yaml(self,file_path : Path):
        with open(file_path,"r") as f:
            return yaml.safe_load(f)
        
    def get_dataIngestionConfig(self)->DataIngestionConfig :
        ingestion = self.config["data_ingestion"]
        os.makedirs(ingestion["root_dir"], exist_ok=True)

        return DataIngestionConfig(
            root_dir= Path(ingestion["root_dir"]),
            source_data=Path(ingestion["source_data"]),
            train_data_path=Path(ingestion["train_data_path"]),
            test_data_path=Path(ingestion["test_data_path"])
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        validation = self.config["data_validation"]

        os.makedirs(validation["root_dir"], exist_ok=True)

        return DataValidationConfig(
            root_dir=Path(validation["root_dir"]),
            train_data_path=Path(validation["train_data_path"]),
            schema_file=Path(validation["schema_file"]),
            status_file=Path(validation["status_file"])
        )
    