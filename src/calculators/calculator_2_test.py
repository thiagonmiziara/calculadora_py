from typing import Dict
from .calculator_2 import Calculator2


class MockFlaskRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockFlaskRequest(body={"numbers": [2.12, 4.62, 1.32]})

    calculator_2 = Calculator2()
    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert "data" in formatted_response
    assert "Calculator" in formatted_response["data"]
    assert "result" in formatted_response["data"]
    assert formatted_response["data"]["Calculator"] == 2
    assert formatted_response["data"]["result"] == 0.08
    assert formatted_response == {"data": {"Calculator": 2, "result": 0.08}}
