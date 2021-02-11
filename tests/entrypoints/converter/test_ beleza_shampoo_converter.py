from src.entities.shampoo import Shampoo
from src.entrypoints.converter.beleza_get_shampoo_converter import BelezaGetShampooConverter
from tests.fixtures.beleza_product_fixture import BelezaProductFixture


def test_converter_shampoo(mocker):
    html = BelezaProductFixture(name='Wella Professionals Fusion',
                                price='555.059,90',
                                brand='Wella Professionals',
                                brand_line='Fusion',
                                hair_type='Danificados',
                                size_unit='Miniatura',
                                utility='Força e Resistência',
                                hair_shaft_condition='Quebradiços',
                                texture='Liquido')
    request = mocker.Mock()
    request.text = str(html)
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-shampoo-50ml/'
    shampoo = BelezaGetShampooConverter().to_entity(request)
    assert type(shampoo) == Shampoo


def test_converter_attributes_shampoo(mocker):
    html = BelezaProductFixture(name='Wella Professionals Fusion',
                                price='555.059,90',
                                brand='Wella Professionals',
                                brand_line='Fusion',
                                hair_type='Danificados',
                                size_unit='Miniatura',
                                utility='Força e Resistência',
                                hair_shaft_condition='Quebradiços',
                                texture='Liquido')
    request = mocker.Mock()
    request.text = str(html)
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-shampoo-50ml/'
    shampoo = BelezaGetShampooConverter().to_entity(request)
    assert shampoo.name == 'Wella Professionals Fusion'
    assert shampoo.brand == 'Wella Professionals'
    assert shampoo.brand_line == 'Fusion'
    assert shampoo.price[0].price == 555059.90
    assert shampoo.size == '50ml'
    assert shampoo.utility == 'Força e Resistência'
    assert shampoo.size_unit == 'Miniatura'
    assert shampoo.hair_type == 'Danificados'
    assert shampoo.hair_shaft_condition == 'Quebradiços'
    assert shampoo.url[0].string == 'https://www.belezanaweb.com.br/wella-professionals-fusion-shampoo-50ml/'
    assert shampoo.url[0].source == 'belezanaweb'
    assert shampoo.code[0].code == '52110'
    assert shampoo.texture == 'Liquido'
