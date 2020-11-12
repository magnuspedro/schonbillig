from logger.logging_module import PTLogger
from bs4 import BeautifulSoup

logger = PTLogger(name=__name__)


class GetShampooConverter:
    def toEntity(html):
        soup = BeautifulSoup(html)
        info_label = soup.select(".info-line")
        for info in info_label:
            a = info.span.text
            logger.info(a)
