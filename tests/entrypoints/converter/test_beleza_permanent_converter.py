from src.entities.permanent import Permanent
from src.entrypoints.converter.beleza_get_permanent_converter import BelezaGetPermanentConverter
from tests.fixtures.beleza_product_fixture import BelezaProductFixture


def test_converter_permanent(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-permanent-50ml/'
    permanent = BelezaGetPermanentConverter().to_entity(request)
    assert type(permanent) == Permanent


def test_converter_attributes_permanent(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-permanent-50ml/'
    permanent = BelezaGetPermanentConverter().to_entity(request)
    assert permanent.name == 'Wella Professionals Fusion'
    assert permanent.brand == 'Wella Professionals'
    assert permanent.brand_line == 'Fusion'
    assert permanent.price[0].price == 555059.90
    assert permanent.size == '50ml'
    assert permanent.utility == 'Força e Resistência'
    assert permanent.size_unit == 'Miniatura'
    assert permanent.hair_type == 'Danificados'
    assert permanent.hair_shaft_condition == 'Quebradiços'
    assert permanent.url[0].string == 'https://www.belezanaweb.com.br/wella-professionals-fusion-permanent-50ml/'
    assert permanent.url[0].source == 'belezanaweb'
    assert permanent.code[0].code == '52110'
    assert permanent.texture == 'Liquido'
    assert permanent.products_for == ['Maciez e Desembaraço', 'Reparação de Danos']
