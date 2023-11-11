import pytest
from src.ej3 import cuentaRegresiva

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (9, "1, 3, 5, 7, 9"),
        (8, "1, 3, 5, 7")
    ]
)
def test_cuentaRegresiva_params(input_n, expected):
    assert cuentaRegresiva(input_n) == expected

def test_cuentaRegresiva_ValueError():
    with pytest.raises(ValueError):
        cuentaRegresiva()