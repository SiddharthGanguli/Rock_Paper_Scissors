from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_data_dir: Path
    train_dir: Path
    test_dir: Path
    test_size: float
    random_state: int


@dataclass
class DataValidationConfig:
    root_dir: Path
    data_dir: Path
    schema_file: Path
    status_file: Path
    min_images_per_class: int
