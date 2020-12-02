from .spyder import Spyder
from request.beleza_na_web.beleza_na_web import BelezaNaWeb
from request.request import Request
from converter.get_shampoo_converter import GetShampooConverter
from logger.logging_module import PTLogger

logger = PTLogger(name = __name__)

class BelezaNaWebSpyder(Spyder):

    urls = {
        'Shampoo': '/api/htmls/showcase?uri=/cabelos/shampoo',
        # 'KitsTratamento': '/api/htmls/showcase?uri=/cabelos/kits-de-tratamento',
        # 'Condicionador': '/api/htmls/showcase?uri=/cabelos/condicionador',
        # 'Tratamento': '/api/htmls/showcase?uri=/cabelos/tratamento',
        # 'LeaveIneCremeParaPentear': '/api/htmls/showcase?uri=/cabelos/leave-in-e-creme-para-pentear',
        # 'Finalizador': '/api/htmls/showcase?uri=/cabelos/finalizador',
        # 'Modelador': '/api/htmls/showcase?uri=/cabelos/modelador',
        # 'EscovaProgressiva': '/api/htmls/showcase?uri=/cabelos/escova-progressiva',
        # 'Acessorios': '/api/htmls/showcase?uri=/cabelos/acessorios',
        # 'Coloracao': '/api/htmls/showcase?uri=/cabelos/coloracao',
    }
    base_url = 'https://www.belezanaweb.com.br'


    def start_request(self):
        for requests in BelezaNaWeb(self.urls, self.base_url).start_request():
            for request in requests:
                response = Request(self.base_url+request).request()
                if response.ok:
                    yield response

    def parse(self):
        for request in self.start_request():
            logger.info('Converting request')
            logger.info(GetShampooConverter().to_entity(request))
            logger.info('Converted successfully')