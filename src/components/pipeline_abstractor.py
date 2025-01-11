from abc import ABC, abstractmethod
from pathlib import Path

class DataPipeline(ABC):
    """
    Abstract base class for pipeline components.
    """

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir

    @abstractmethod
    def setup(self, *args, **kwargs):
        """Prepare resources for the component."""
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Main logic for the component."""
        pass

    @abstractmethod
    def teardown(self, *args, **kwargs):
        """Release resources after execution."""
        pass

    def validate(self, *args, **kwargs):
        """Optional validation logic (default: no-op)."""
        pass
