from loja.produto import Camiseta
from loja.produto import Calca
import pytest

def test_camiseta_herda_a_validacao_do_produto():
    with pytest.raises(ValueError):
        Camiseta("Camiseta Básica", -10, "M", "curta")

def test_manga_invalida():
    with pytest.raises(ValueError):
        Camiseta("Camiseta básica", 39.90, "M", "regata")

def test_calca_herda_a_validacao_do_produto():
    with pytest.raises(ValueError):
        Calca("Calça Jeans Preta", -25, "M", "Calça")

def test_calca_invalida():
    with pytest.raises(ValueError):
        Calca("Short NIKE GYM", 99.90, "P", "Shorts")