from src.entities.dye import Dye
from src.entrypoints.converter.beleza_dye_converter import BelezaGetDyeConverter
from tests.fixtures.beleza_dye_fixture import BelezaDyeFixture


def test_converter_dye(mocker):
    html = BelezaDyeFixture().html
    request = mocker.Mock()
    request.text = str(html)
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-color-touch-60-louro-escuro-tonalizante-60g/'
    dye = BelezaGetDyeConverter().to_entity(request)
    assert type(dye) == Dye


def test_converter_attributes_dye(mocker):
    html = BelezaDyeFixture().html
    request = mocker.Mock()
    request.text = str(html)
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-color-touch-60-louro-escuro-tonalizante-60g/'
    dye = BelezaGetDyeConverter().to_entity(request)
    assert dye.name == 'Wella Professionals Color Touch 6/0 Louro Escuro'
    assert dye.brand == 'Wella Professionals'
    assert dye.brand_line == 'Color Touch'
    assert dye.price[0].price == 37.90
    assert dye.size == '60g'
    assert dye.url[0].string == 'https://www.belezanaweb.com.br/wella-professionals-color-touch-60-louro-escuro-tonalizante-60g/'
    assert dye.url[0].source == 'belezanaweb'
    assert dye.code[0].code == '63279'
    assert dye.color == 'Louro escuro'
    assert dye.color_number == '6/0 Louro Escuro'
