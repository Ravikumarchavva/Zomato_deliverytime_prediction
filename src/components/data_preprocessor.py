import polars as pl
import numpy as np
from components.pipeline_abstractor import DataPipeline
from components.data_ingestion import DataIngestion
from pathlib import Path

# Delivery_person_Age	Delivery_person_Ratings	Restaurant_latitude	Restaurant_longitude	Delivery_location_latitude	Delivery_location_longitude	Order_Date	Time_Orderd	Time_Order_picked	Weather_conditions	Road_traffic_density	Vehicle_condition	Type_of_order	Type_of_vehicle	multiple_deliveries	Festival	City	Time_taken (min)
# f64	f64	f64	f64	f64	f64	str	str	str	str	str	i64	str	str	f64	str	str	i64


# DataPreprocessor class
class DataPreprocessor(DataPipeline):
    """
    Component for data preprocessing.
    """

    def __init__(self, data_ingestor: DataIngestion, data_path: Path):
        """
        Initialize the DataPreprocessor component.

        Args:
            data_ingestor (DataIngestor): The data ingestor component.
            data_path (str): The path to the data file.
        """
        self.data_ingestor = data_ingestor
        self.data_path = data_path
        self.data = None



    def load_data(self):
        """
        Load the data from the data file.

        Returns:
            pl.DataFrame: The loaded data.
        """
        self.data = pl.read_csv(self.data_path)
        return self.data

    def preprocess_data(self):
        """
        Preprocess the data.

        Returns:
            pl.DataFrame: The preprocessed data.
        """
        self.data = self.data.drop(["Order_Date", "Time_Orderd", "Time_Order_picked"])
        self.data = self.data.drop_nulls()
        return self.data

    def run(self):
        """
        Run the data preprocessor component.

        Returns:
            pl.DataFrame: The preprocessed data.
        """
        self.load_data()
        return self.preprocess_data()