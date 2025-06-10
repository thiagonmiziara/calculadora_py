from abc import ABC, abstractmethod
from typing import List


# interfaces driver_handler_interface.py
class DriverHandlerInterface(ABC):
    @abstractmethod
    def standard_deviation(self, numbers: List[float]) -> float:
        raise NotImplementedError

    @abstractmethod
    def variance(self, numbers: List[float]) -> float:
        pass
