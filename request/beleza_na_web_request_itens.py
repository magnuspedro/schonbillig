from requests import Session
from bs4 import BeautifulSoup

class BelezaNaWebRequestItens:
    url = 'https://www.belezanaweb.com.br'
    first_parameters = '&size=36&pagina=1'

    def __init__(self, subitem, link):
        self.subitem = subitem
        self.link = link
        

    def get_next_url(self, page_source):
        """
        Return "Add to watch list" button url.
        """
        soup = BeautifulSoup(page_source, 'html.parser')
        for button in soup.find_all("button", class_='lazyload'):
            return button.get('data-ajax')

    def get_list_url(self, page_source):
        """
        Return "Add to watch list" button url.
        """
        soup = BeautifulSoup(page_source, 'html.parser')
        urls = []
        for link in soup.find_all("a", class_='showcase-item-image'):
            urls.append(link['href'])
        
        return urls

    def request_itens(self):
        with Session() as session:

            urls = []
            response = session.get(self.url + self.link + self.first_parameters)  # visit item page and scrape button
            while response.ok:
                next_url = self.get_next_url(response.content)

                if next_url is None:
                    break

                urls.extend(self.get_list_url(response.content))
                #print('Url is:', next_url)

                response = session.get(self.url + next_url)  # add item to watch list
                
            #print(f"{self.subitem} - QTDE: {len(urls)}")
            return self.subitem, urls
