import pytest
from src.ej1 import pedirEdad

@pytest.mark.parametrize(
    "input_edad, expected",
    [
        (10, "1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    ]
)
def test_pedirEdad_params(input_edad, expected):
    assert pedirEdad(input_edad) == expected

def test_pedirEdad_ValueError():
    with pytest.raises(ValueError):
        pedirEdad(0)