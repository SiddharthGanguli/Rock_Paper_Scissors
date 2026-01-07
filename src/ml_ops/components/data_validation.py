import os
import logging
import yaml
from pathlib import Path
from PIL import Image

from ml_ops.entity.config_entity import DataValidationConfig

logging.basicConfig(level=logging.INFO)


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def _read_schema(self):
        with open(self.config.schema_file, "r") as f:
            return yaml.safe_load(f)

    def _get_image_files(self, class_dir):
        return [
            i for i in class_dir.iterdir()
            if i.is_file()
        ]

    def initiate_data_validation(self) -> bool:
        logging.info("Starting image data validation")

        schema = self._read_schema()
        expected_classes = schema["classes"]
        image_rules = schema["image"]

        validation_status = True

        data_dir = Path(self.config.data_dir)
        class_dirs = [i for i in data_dir.iterdir() if i.is_dir()]

        class_names = [i.name for i in class_dirs]
        if set(class_names) != set(expected_classes):
            logging.error("Class folders do not match schema")
            validation_status = False

        for class_dir in class_dirs:
            images = self._get_image_files(class_dir)
            if len(images) < self.config.min_images_per_class:
                logging.error(
                    f"Not enough images in {class_dir.name}: {len(images)}"
                )
                validation_status = False

            for img_path in images:
                ext = img_path.suffix.lower().replace(".", "")
                if ext not in image_rules["allowed_extensions"]:
                    logging.error(f"Invalid image format: {img_path}")
                    validation_status = False
                    continue

                try:
                    with Image.open(img_path) as img:
                        width, height = img.size

                        if not (
                            image_rules["min_width"] <= width <= image_rules["max_width"]
                            and image_rules["min_height"] <= height <= image_rules["max_height"]
                        ):
                            logging.error(f"Invalid image size: {img_path}")
                            validation_status = False

                        if img.mode != "RGB":
                            logging.error(f"Invalid image channels: {img_path}")
                            validation_status = False

                except Exception:
                    logging.error(f"Corrupt image: {img_path}")
                    validation_status = False
        os.makedirs(self.config.root_dir, exist_ok=True)
        with open(self.config.status_file, "w") as f:
            f.write(str(validation_status))

        if validation_status:
            logging.info("Data validation passed")
        else:
            logging.error("Data validation failed")

        return validation_status
