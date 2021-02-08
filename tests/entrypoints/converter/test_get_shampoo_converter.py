import pytest

from src.entities.shampoo import Shampoo
from src.entrypoints.converter.get_shampoo_beleza_converter import GetShampooBelezaConverter
from tests.fixtures.shampoo import shampoo_wella


def test_converter_shampoo(mocker):
    html = shampoo_wella()
    request = mocker.Mock()
    request.text = html
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-shampoo-50ml/'
    shampoo = GetShampooBelezaConverter().to_entity(request)
    assert type(shampoo) == Shampoo


def test_converter_attributes_shampoo(mocker):
    html = shampoo_wella()
    request = mocker.Mock()
    request.text = html
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-shampoo-50ml/'
    shampoo = GetShampooBelezaConverter().to_entity(request)
    assert shampoo.name == 'Wella Professionals Fusion'
    assert shampoo.brand == 'Wella Professionals'
    assert shampoo.brand_line == 'Fusion'
    assert shampoo.price[0].price == 555059.90
    assert shampoo.vegan == False
    assert shampoo.size == '50ml'
    assert shampoo.utility == 'Força e Resistência'
    assert shampoo.size_unit == 'Miniatura'
    assert shampoo.hair_type =='Danificados'
    assert shampoo.hair_shaft_condition =='Quebradiços'
    assert shampoo.url[0].string == 'https://www.belezanaweb.com.br/wella-professionals-fusion-shampoo-50ml/'
    assert shampoo.url[0].source == 'belezanaweb'
    assert shampoo.code[0].code == '52110'
