from enum import Enum


class Config(Enum):
    BELEZA_PARAMAS = '&size=36&pagina=1'
    BELEZA_BASE_URL = 'https://www.belezanaweb.com.br'
    REQUEST_RETRY = 10
    WAITING_TIME = 2
    BELEZA_URLS = {
        'shampoo': '/api/htmls/showcase?uri=/cabelos/shampoo',
        'KitsTratamento': '/api/htmls/showcase?uri=/cabelos/kits-de-tratamento',
        'conditioner': '/api/htmls/showcase?uri=/cabelos/condicionador',
        'Tratamento': '/api/htmls/showcase?uri=/cabelos/tratamento',
        'LeaveIneCremeParaPentear': '/api/htmls/showcase?uri=/cabelos/leave-in-e-creme-para-pentear',
        'finisher': '/api/htmls/showcase?uri=/cabelos/finalizador',
        'Modelador': '/api/htmls/showcase?uri=/cabelos/modelador',
        'EscovaProgressiva': '/api/htmls/showcase?uri=/cabelos/escova-progressiva',
        'Acessorios': '/api/htmls/showcase?uri=/cabelos/acessorios',
        'Coloracao': '/api/htmls/showcase?uri=/cabelos/coloracao',
    }
    IKESAKI_BASE_URL = 'https://www.ikesaki.com.br'
    IKESAKI_PARAMS = '&PageNumber=1'
    IKESAKI_URLS = {
        'shampoo': '/buscapagina?fq=C:/1000004/1000013/&PS=48&sl=dc9f5d37-edae-4e7a-8f60-730b8ecb09ec&cc=48&sm=0'
    }
