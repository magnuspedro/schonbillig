from src.entities.treatment import Treatment
from src.entrypoints.converter.get_treatment_beleza_converter import GetTreatmentBelezaConverter
from tests.fixtures.beleza_product_fixture import BelezaProductFixture


def test_converter_treatment(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-treatment-50ml/'
    treatment = GetTreatmentBelezaConverter().to_entity(request)
    assert type(treatment) == Treatment


def test_converter_attributes_treatment(mocker):
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
    request.url = 'https://www.belezanaweb.com.br/wella-professionals-fusion-treatment-50ml/'
    treatment = GetTreatmentBelezaConverter().to_entity(request)
    assert treatment.name == 'Wella Professionals Fusion'
    assert treatment.brand == 'Wella Professionals'
    assert treatment.brand_line == 'Fusion'
    assert treatment.price[0].price == 555059.90
    assert treatment.vegan == False
    assert treatment.size == '50ml'
    assert treatment.utility == 'Força e Resistência'
    assert treatment.size_unit == 'Miniatura'
    assert treatment.hair_type == 'Danificados'
    assert treatment.hair_shaft_condition == 'Quebradiços'
    assert treatment.url[0].string == 'https://www.belezanaweb.com.br/wella-professionals-fusion-treatment-50ml/'
    assert treatment.url[0].source == 'belezanaweb'
    assert treatment.code[0].code == '52110'
    assert treatment.texture == 'Liquido'
