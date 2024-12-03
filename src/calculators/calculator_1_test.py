from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1


class MockFlaskRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculator_1():
    mock_request = MockFlaskRequest(body={"number": 1})
    calc = Calculator1()

    response = calc.calculate(mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    assert response["data"]["Calculator"] == 1
    assert response["data"]["result"] == 14.25


def test_calculate_whith_body_error():
    mock_request = MockFlaskRequest(body={"info": 1})
    calc = Calculator1()

    with raises(Exception) as excinfo:
        calc.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"
