from scripts.parser import Parser
from json_dump import json_dump

def main():
    output_list = Parser.uzgov_parser(uzgov_base_url) + Parser.railway_parser(raiwaysupply_base_url)
    json_dump(output_list, 'json/info.json')

uzgov_base_url = 'https://www.uz.gov.ua'
raiwaysupply_base_url = 'https://www.railway.supply/uk/news-ua/'

main()