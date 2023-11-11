import pytest
from src.ej2 import numerosImpares

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (9, "1, 3, 5, 7, 9"),
        (8, "1, 3, 5, 7")
    ]
)
def test_numerosImpares_params(input_n, expected):
    assert numerosImpares(input_n) == expected

def test_numerosImpares_ValueError():
    with pytest.raises(ValueError):
        numerosImpares(-1)