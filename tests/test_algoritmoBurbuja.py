import pytest
from src.algoritmoBurbuja import ordLista

@pytest.mark.parametrize(
    "input_a, expected",
    [
        ([6, 8, 2, 9, 34], [2, 6, 8, 9, 34]),
        ([45, 23], [23, 45])  
    ]
)
def test_ordLista_params(input_a, expected):
    assert ordLista(input_a) == expected