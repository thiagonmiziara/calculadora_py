from typing import Dict
from .calculator_2 import Calculator2


class MockFlaskRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockFlaskRequest(body={"numbers": [1.33, 2.55, 3.69]})

    calculator_2 = Calculator2()
    calculator_2.calculate(mock_request)
