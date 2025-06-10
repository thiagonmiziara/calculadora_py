from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3


class MockFlaskRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 0.08


class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 100000


def test_calculate_with_variance_error():
    mock_request = MockFlaskRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "Falha no processo: variancia menor que multiplicação"


def test_calculate():
    mock_request = MockFlaskRequest(body={"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())

    response = calculator_3.calculate(mock_request)
    assert response == {"data": {"Calculator": 3, "value": 100000, "success": True}}
