import pytest
from src.config.exceptions.page_not_found_exception import PageNotFoundException
from src.entities.enum.products_strategy import ProductsStrategy
from src.gateway.providers.beleza.beleza_spyder import \
    BelezaSpyder


def test_product_not_found(mocker):
    with pytest.raises(PageNotFoundException):
        mocker.patch(
            'src.gateway.providers.beleza.beleza_spyder.BelezaSpyder.start_request').side_effect = PageNotFoundException
        BelezaSpyder().start_request(ProductsStrategy.SHAMPOO_BELEZA)


def test_without_product():
    with pytest.raises(TypeError):
        BelezaSpyder().start_request()


def test_individual_product(mocker):
    url = '/wella-professionals-fusion-shampoo-50ml/'
    mocker.patch('src.gateway.providers.beleza.beleza_request_items.BelezaRequestItems.request_items', lambda x: [url])
    request_moker = mocker.patch('src.gateway.bases.request.Request.request')
    request_moker.return_value.ok = True
    assert len(BelezaSpyder().start_request(ProductsStrategy.SHAMPOO_BELEZA)) == 1


def test_fail_individual_product(mocker, requests_mock):
    url = '/wella-professionals-fusion-shampoo-50ml/'
    mocker.patch('src.gateway.providers.beleza.beleza_request_items.BelezaRequestItems.request_items', lambda x: [url])
    request_moker = mocker.patch('src.gateway.bases.request.Request.request')
    request_moker.return_value.ok = False
    assert len(BelezaSpyder().start_request(ProductsStrategy.SHAMPOO_BELEZA)) == 0