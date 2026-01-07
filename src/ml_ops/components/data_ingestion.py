import os
import shutil
import logging
from pathlib import Path
from sklearn.model_selection import train_test_split

from ml_ops.entity.config_entity import DataIngestionConfig

logging.basicConfig(level=logging.INFO)


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def _get_images(self, class_dir: Path):
        return [img for img in class_dir.iterdir() if img.is_file()]

    def initiate_data_ingestion(self):
        logging.info("Starting image data ingestion")

        source_dir = Path(self.config.source_data_dir)

        os.makedirs(self.config.train_dir, exist_ok=True)
        os.makedirs(self.config.test_dir, exist_ok=True)

        for class_dir in source_dir.iterdir():
            if not class_dir.is_dir():
                continue

            images = self._get_images(class_dir)

            train_imgs, test_imgs = train_test_split(
                images,
                test_size=self.config.test_size,
                random_state=self.config.random_state
            )

            train_class_dir = Path(self.config.train_dir) / class_dir.name
            test_class_dir = Path(self.config.test_dir) / class_dir.name

            os.makedirs(train_class_dir, exist_ok=True)
            os.makedirs(test_class_dir, exist_ok=True)

            for img in train_imgs:
                shutil.copy(img, train_class_dir / img.name)

            for img in test_imgs:
                shutil.copy(img, test_class_dir / img.name)

            logging.info(
                f"Class '{class_dir.name}': "
                f"{len(train_imgs)} train, {len(test_imgs)} test images"
            )

        logging.info("Data ingestion completed successfully")

        return self.config.train_dir, self.config.test_dir
