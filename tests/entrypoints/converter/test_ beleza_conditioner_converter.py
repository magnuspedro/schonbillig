from src.entities.conditioner import Conditioner
from src.entrypoints.converter.get_conditioner_beleza_conevert import GetConditionerBelezaConverter
from tests.fixtures.beleza_product_fixture import BelezaProductFixture


def test_converter_conditioner(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-conditioner-50ml/'
    conditioner = GetConditionerBelezaConverter().to_entity(request)
    assert type(conditioner) == Conditioner


def test_converter_attributes_conditioner(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-conditioner-50ml/'
    conditioner = GetConditionerBelezaConverter().to_entity(request)
    assert conditioner.name == 'Wella Professionals Fusion'
    assert conditioner.brand == 'Wella Professionals'
    assert conditioner.brand_line == 'Fusion'
    assert conditioner.price[0].price == 555059.90
    assert conditioner.vegan == False
    assert conditioner.size == '50ml'
    assert conditioner.utility == 'Força e Resistência'
    assert conditioner.size_unit == 'Miniatura'
    assert conditioner.hair_type == 'Danificados'
    assert conditioner.hair_shaft_condition == 'Quebradiços'
    assert conditioner.url[0].string == 'https://www.belezanaweb.com.br/wella-professionals-fusion-conditioner-50ml/'
    assert conditioner.url[0].source == 'belezanaweb'
    assert conditioner.code[0].code == '52110'
    assert conditioner.texture == 'Liquido'
