import pytest
from src.gateway.providers.beleza.beleza_request_items import \
    BelezaRequestItems
from tenacity import RetryError
from src.config.exceptions.page_not_found_exception import PageNotFoundException


def test_request_items(requests_mock):
    link = '''<a href="/truss-specific-equilibrio-shampoo-300ml/"
    title="Truss Equilibrium - Shampoo 300ml"
    class="showcase-item-image ">'''
    source = 'https://www.belezanaweb.com.br/api/htmls/showcase?uri=/cabelos/'
    product = 'shampoo'
    params = '&size=36&pagina=1'
    requests_mock.get(source + product + params, status_code=200, text=link)
    assert list == type(BelezaRequestItems(source, params, product).request_items())

def test_fail_request_items(mocker):
    source = 'https://www.belezanaweb.com.br/api/htmls/showcase?uri=/cabelos/'
    product = 'shampoo'
    params = '&size=36&pagina=1'
    request_mocker = mocker.patch('src.gateway.providers.bases.request.Request.request')
    request_mocker.side_effect = RetryError(last_attempt=10)
    assert len(BelezaRequestItems(source, params, product).request_items()) == 0


def test_get_next_url():
    button = '''<button class="btn btn-outline-secondary btn-bolder btn-load-more js-load-more m-a lazyload"
    data-outer-html="true"
    data-ajax="/api/htmls/showcase?uri=/cabelos/shampoo&amp;size=36&amp;pagina=2">
    Carregar mais produtos</button>'''
    source = 'https://www.belezanaweb.com.br/api/htmls/showcase?uri=/cabelos/'
    product = 'shampoo'
    params = '&size=36&pagina=1'
    assert str == type(BelezaRequestItems(source, params, product).get_next_url(button))


def test_fail_get_next_url():
    button = '''<button class="btn btn-outline-secondary btn-bolder btn-load-more js-load-more m-a lazyload"
    data-outer-html="true">
    Carregar mais produtos</button>'''
    source = 'https://www.belezanaweb.com.br/api/htmls/showcase?uri=/cabelos/'
    product = 'shampoo'
    params = '&size=36&pagina=1'
    assert None == BelezaRequestItems(source, params, product).get_next_url(button)


def test_get_list_url():
    link = '''<a href="/truss-specific-equilibrio-shampoo-300ml/"
    title="Truss Equilibrium - Shampoo 300ml"
    class="showcase-item-image ">'''
    source = 'https://www.belezanaweb.com.br/api/htmls/showcase?uri=/cabelos/'
    product = 'shampoo'
    params = '&size=36&pagina=1'
    assert len(BelezaRequestItems(source, params, product).get_list_url(link)) == 1

def test_fail_get_list_url():
    link = '''<button class="btn btn-outline-secondary btn-bolder btn-load-more js-load-more m-a lazyload"
    data-outer-html="true">
    Carregar mais produtos</button>'''
    source = 'https://www.belezanaweb.com.br/api/htmls/showcase?uri=/cabelos/'
    product = 'shampoo'
    params = '&size=36&pagina=1'
    assert len(BelezaRequestItems(source, params, product).get_list_url(link)) == 0
