from logger.logging_module import PTLogger
from request.beleza_na_web_request_itens import BelezaNaWebRequestItens

logger = PTLogger(name=__name__)

class BelezaNaWebLinks():
    #logger.info(f'Getting links for requesting to {__name__}')
    def __init__(self):
        self.urls = {
            "Shampoo": "/api/htmls/showcase?uri=/cabelos/shampoo",
            "KitsTratamento": "/api/htmls/showcase?uri=/cabelos/kits-de-tratamento",
            "Condicionador": "/api/htmls/showcase?uri=/cabelos/condicionador",
            "Tratamento": "/api/htmls/showcase?uri=/cabelos/tratamento",
            "LeaveIneCremeParaPentear": "/api/htmls/showcase?uri=/cabelos/leave-in-e-creme-para-pentear",
            "Finalizador": "/api/htmls/showcase?uri=/cabelos/finalizador",
            "Modelador": "/api/htmls/showcase?uri=/cabelos/modelador",
            "EscovaProgressiva": "/api/htmls/showcase?uri=/cabelos/escova-progressiva",
            "Acessorios": "/api/htmls/showcase?uri=/cabelos/acessorios",
            "Coloracao": "/api/htmls/showcase?uri=/cabelos/coloracao",
        }

    def start_request(self, urls=None):
        if urls is None:
            urls = self.urls
        
        for key, url in urls.items():
            print(f"{key}, {url}")
            #logger.debug(f'[StartRequest]', extra={'mdc': {'url': url}})
            yield BelezaNaWebRequestItens(key, url).request_itens()

    