from src.entities.shaper import Shaper
from src.entrypoints.converter.get_shaper_beleza_converter import GetShaperBelezaConverter
from tests.fixtures.beleza_product_fixture import BelezaProductFixture


def test_converter_shaper(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-shaper-50ml/'
    shaper = GetShaperBelezaConverter().to_entity(request)
    assert type(shaper) == Shaper


def test_converter_attributes_shaper(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-shaper-50ml/'
    shaper = GetShaperBelezaConverter().to_entity(request)
    assert shaper.name == 'Wella Professionals Fusion'
    assert shaper.brand == 'Wella Professionals'
    assert shaper.brand_line == 'Fusion'
    assert shaper.price[0].price == 555059.90
    assert shaper.vegan == False
    assert shaper.size == '50ml'
    assert shaper.utility == 'Força e Resistência'
    assert shaper.size_unit == 'Miniatura'
    assert shaper.hair_type == 'Danificados'
    assert shaper.hair_shaft_condition == 'Quebradiços'
    assert shaper.url[0].string == 'https://www.belezanaweb.com.br/wella-professionals-fusion-shaper-50ml/'
    assert shaper.url[0].source == 'belezanaweb'
    assert shaper.code[0].code == '52110'
    assert shaper.texture == 'Liquido'
    assert shaper.products_for == ['Maciez e Desembaraço', 'Reparação de Danos']
