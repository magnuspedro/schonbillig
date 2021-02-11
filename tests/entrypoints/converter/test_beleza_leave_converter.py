from src.entities.leave import Leave
from src.entrypoints.converter.beleza_get_leave_converter import BelezaGetLeaveConverter
from tests.fixtures.beleza_product_fixture import BelezaProductFixture


def test_converter_leave(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-leave-50ml/'
    leave = BelezaGetLeaveConverter().to_entity(request)
    assert type(leave) == Leave


def test_converter_attributes_leave(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-leave-50ml/'
    leave = BelezaGetLeaveConverter().to_entity(request)
    assert leave.name == 'Wella Professionals Fusion'
    assert leave.brand == 'Wella Professionals'
    assert leave.brand_line == 'Fusion'
    assert leave.price[0].price == 555059.90
    assert leave.size == '50ml'
    assert leave.utility == 'Força e Resistência'
    assert leave.size_unit == 'Miniatura'
    assert leave.hair_type == 'Danificados'
    assert leave.hair_shaft_condition == 'Quebradiços'
    assert leave.url[0].string == 'https://www.belezanaweb.com.br/wella-professionals-fusion-leave-50ml/'
    assert leave.url[0].source == 'belezanaweb'
    assert leave.code[0].code == '52110'
    assert leave.texture == 'Liquido'
    assert leave.products_for == ['Maciez e Desembaraço', 'Reparação de Danos']
