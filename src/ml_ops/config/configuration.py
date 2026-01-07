import os
from pathlib import Path
import yaml

from ml_ops.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig
)


class ConfigurationManager:

    def __init__(self, config_filepath: Path):
        self.config = self._read_yaml(config_filepath)

    def _read_yaml(self, file_path: Path):
        with open(file_path, "r") as f:
            return yaml.safe_load(f)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        ingestion = self.config["data_ingestion"]

        os.makedirs(ingestion["root_dir"], exist_ok=True)

        return DataIngestionConfig(
            root_dir=Path(ingestion["root_dir"]),
            source_data_dir=Path(ingestion["source_data_dir"]),
            train_dir=Path(ingestion["train_dir"]),
            test_dir=Path(ingestion["test_dir"]),
            test_size=ingestion["test_size"],
            random_state=ingestion["random_state"]
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        validation = self.config["data_validation"]

        os.makedirs(validation["root_dir"], exist_ok=True)

        return DataValidationConfig(
            root_dir=Path(validation["root_dir"]),
            data_dir=Path(validation["data_dir"]),
            schema_file=Path(validation["schema_file"]),
            status_file=Path(validation["status_file"]),
            min_images_per_class=validation["min_images_per_class"]
        )
