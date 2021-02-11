from src.entities.finisher import Finisher
from src.entrypoints.converter.beleza_get_finisher_converter import BelezaGetFinisherConverter
from tests.fixtures.beleza_product_fixture import BelezaProductFixture


def test_converter_finisher(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-finisher-50ml/'
    finisher = BelezaGetFinisherConverter().to_entity(request)
    assert type(finisher) == Finisher


def test_converter_attributes_finisher(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-finisher-50ml/'
    finisher = BelezaGetFinisherConverter().to_entity(request)
    assert finisher.name == 'Wella Professionals Fusion'
    assert finisher.brand == 'Wella Professionals'
    assert finisher.brand_line == 'Fusion'
    assert finisher.price[0].price == 555059.90
    assert finisher.size == '50ml'
    assert finisher.utility == 'Força e Resistência'
    assert finisher.size_unit == 'Miniatura'
    assert finisher.hair_type == 'Danificados'
    assert finisher.hair_shaft_condition == 'Quebradiços'
    assert finisher.url[0].string == 'https://www.belezanaweb.com.br/wella-professionals-fusion-finisher-50ml/'
    assert finisher.url[0].source == 'belezanaweb'
    assert finisher.code[0].code == '52110'
    assert finisher.texture == 'Liquido'
