import pytest
from src.ej4 import pedirNumero

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (6, 6),
        (5, 5),
        (125, 125)
    ]
)
def test_pedirNumero_params(input_n, expected):
    assert pedirNumero(input_n) == expected

def test_pedirNumero_ValueError():
    with pytest.raises(ValueError):
        pedirNumero(3.8)