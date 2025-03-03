import logging

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from requests.exceptions import ConnectionError

# CONFIGURACAO DO LOGGING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def extract_html(url):
    """Extrai o HMTL de uma URL"""
    try:
        response = requests.get(url)
        soup = bs(response.text, "html.parser")
        logger.info(f"Extracao HTML realizada com sucesso --- {url}")
        return soup
    except ConnectionError as e:
        logger.error(f"Erro ao conectar url --- {e}")


def extract_country_population_save_csv(soup):
    """Extrai dados da tabela no html"""
    tab = soup.find("table")
    linhas = tab.find_all("tr")
    countries = []
    for row in linhas:
        try:
            data = row.find_all("td")
            if data:
                country = data[1].text.strip()
                population = data[2].text.strip()
                rate = data[3].text.strip()
                countries.append(
                    {"country": country, "population": population, "rate": rate}
                )
        except AttributeError as e:
            logger.error(f"Erro ao extrair dados da tabela --- {e}")
            continue

    countries = pd.DataFrame(countries)
    countries.to_csv("populacao_paises.csv", index=False)
    num_rows = len(countries)
    logger.info(f"Dados da tabela extraidos com sucesso --- {num_rows} linhas")


if __name__ == "__main__":
    URL = "https://www.worldometers.info/world-population/population-by-country/"

    website_html = extract_html(URL)
    file = extract_country_population_save_csv(website_html)
