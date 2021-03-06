"""
    Module contain functions for sync parsing pages of openheritage3d.org
"""
import re
from typing import List

from bs4 import BeautifulSoup
import requests

# establishing session
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
})

OTPBANK_HTML = 'https://rybka.otpbank.ru/guaranteed_prizes'


# Parse openheritage3d.org/data projects page
# to list of projects urls -> ['url1', 'url2', ..., 'url(n)']
# return list of projects urls
# def parse_data_page(url: str = OTPBANK_HTML) -> List[str]:
#     list_of_projects_urls = list()
#     text = session.get(url).text
#     soup = BeautifulSoup(text, 'html.parser')
#     projects_list = soup.find_all(href=re.compile("project.php"))
#     for project in projects_list:
#         list_of_projects_urls.append(OTPBANK_HTML + '/' + project.get('href'))
#
#     return list_of_projects_urls


# Parse single project url (example: https://openheritage3d.org/project.php?id=ws0a-3g91)
#  to dict (example: project_dict(project_name:'Bagan - Loka Hteik Pan',
#                                 DOI:'https://doi.org/10.26301/05r8-we91',
#                                 ...)
# return project_dict
def parse_single_project(url: str) -> dict[str: str]:
    prize_dict = dict()
    text = session.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    print(soup)
    # add elements from "General Attributes" table to prize_dict
    prize_dict['prizes'] = soup.find_all(class_='info small-text')
    # prize_dict['DOI'] = soup.find_all('table')[0].find(string='DOI').find_parent(
    #     'td').a.get('href').lstrip()
    # prize_dict['status'] = soup.find_all('table')[0].find(string='Status').find_parent(
    #     'td').find_next_sibling('td').text
    print(prize_dict)
    # add elements from "Background" table to prize_dict
    # table_background = soup.find(
    #     lambda tag: tag.name == 'table' and 'Background' in tag.text)
    # prize_dict['collection_date'] = table_background.find(
    #     string='Collection Date').find_parent('td').find_next_sibling('td').text
    # prize_dict['publication_date'] = table_background.find(string='Publication Date').find_parent(
    #     'td').find_next_sibling('td').text

    # add elements from "Data Types" table to prize_dict
    # table_datatype = soup.find(
    #     lambda tag: tag.name == 'table' and 'Device Name' in tag.text)
    # data_types = table_datatype.find_all('tr')

    # for item in data_types:
    #     key = item.td.text
    #     value = item.td.find_next_sibling('td').text
    #     prize_dict.update(((key, value),))

    return prize_dict


if __name__ == '__main__':
    parse_single_project(OTPBANK_HTML)
