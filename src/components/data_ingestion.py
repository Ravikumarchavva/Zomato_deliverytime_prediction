from components.pipeline_abstractor import DataPipeline
import polars as pl
from pathlib import Path

import sys
sys.path.append('..')
from configs.configs import ROOT_DIR

# DataIngestion class
class DataIngestion(DataPipeline):
    """
    Component for data ingestion.
    """

    def __init__(self, raw_data_dir: Path):
        super().__init__(data_dir=raw_data_dir)

    # def load_data(self, file_name: str) -> pl.DataFrame:
    #     """
    #     Load data from a CSV file.
    #     """
    #     file_path = self.data_dir / file_name
    #     return pl.read_csv(file_path)

    # def execute(self, file_name: str) -> pl.DataFrame:
    #     """
    #     Execute the data ingestion process.
    #     """
    #     return self.load_data(file_name)

    # def validate(self, file_name: str):
    #     """
    #     Validate the input data file (example: check if the file exists).
    #     """
    #     file_path = self.data_dir / file_name
    #     if not file_path.exists():
    #         raise FileNotFoundError(f"File not found: {file_path}")
    #     print(f"Validation successful: {file_path}")

    def load_data(self, file_name: str) -> pl.DataFrame:
        """
        Load data from a CSV file.
        """
        file_path = self.data_dir / file_name
        return pl.read_csv(file_path)
    
    def setup(self, *args, **kwargs):
        """Prepare resources for the component."""
        pass

    def execute(self, *args, **kwargs):
        """Main logic for the component."""
        pass

    def teardown(self, *args, **kwargs):
        """Release resources after execution."""
        pass

    def validate(self, *args, **kwargs):
        """Optional validation logic (default: no-op)."""
        pass
    

if __name__ == '__main__':
    # Path to the raw data directory
    RAW_DATA_DIR = ROOT_DIR / 'data' / 'raw_data'

    data_ingestion = DataIngestion(raw_data_dir=RAW_DATA_DIR)
    df = data_ingestion.load_data('Zomato Dataset.csv')
    print(df)