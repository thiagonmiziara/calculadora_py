from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from .calculator_2 import Calculator2


class MockFlaskRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def standard_deviation(self, numbers: List[float]) -> float:
        return 0.08


def test_calculate_integration():
    mock_request = MockFlaskRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver_handler = NumpyHandler()
    calculator_2 = Calculator2(driver_handler)
    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert "data" in formatted_response
    assert "Calculator" in formatted_response["data"]
    assert "result" in formatted_response["data"]
    assert formatted_response["data"]["Calculator"] == 2
    assert formatted_response["data"]["result"] == 0.08
    assert formatted_response == {"data": {"Calculator": 2, "result": 0.08}}


def test_calculate():
    mock_request = MockFlaskRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver_handler = MockDriverHandler()
    calculator_2 = Calculator2(driver_handler)
    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert "data" in formatted_response
    assert "Calculator" in formatted_response["data"]
    assert "result" in formatted_response["data"]
    assert formatted_response["data"]["Calculator"] == 2
    assert formatted_response["data"]["result"] == 12.5
    assert formatted_response == {"data": {"Calculator": 2, "result": 12.5}}
