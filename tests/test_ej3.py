import pytest
from src.ej3 import cuentaRegresiva

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (10, "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (3, "3, 2, 1, 0")
    ]
)
def test_cuentaRegresiva_params(input_n, expected):
    assert cuentaRegresiva(input_n) == expected

def test_cuentaRegresiva_Exception():
    with pytest.raises(Exception):
        cuentaRegresiva(0)