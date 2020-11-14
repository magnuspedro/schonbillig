from requests import Session
from bs4 import BeautifulSoup

url = 'https://www.belezanaweb.com.br'
first_call = '/api/htmls/showcase?uri=/cabelos/shampoo&size=36&pagina=1'

def get_next_url(page_source):
    """
    Return "Add to watch list" button url.
    """
    soup = BeautifulSoup(page_source, 'html.parser')
    for button in soup.find_all("button", class_='lazyload'):
        return button.get('data-ajax')

def get_list_url(page_source):
    """
    Return "Add to watch list" button url.
    """
    soup = BeautifulSoup(page_source, 'html.parser')
    urls = []
    for link in soup.find_all("a", class_='showcase-item-image'):
        urls.append(link['href'])
    
    return urls

def main():
    with Session() as session:

        response = session.get(url + first_call)  # visit item page and scrape button
        urls = []
        while response.ok:
            next_url = get_next_url(response.content)

            if next_url is None:
                break

            urls.extend(get_list_url(response.content))
            print('Url is:', next_url)

            response = session.get(url + next_url)  # add item to watch list
            
        print(urls)

if __name__ == '__main__':
    main()