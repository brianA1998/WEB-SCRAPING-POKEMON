"""Este modulo tiene como finalidad obtener el nombre,tipo y especie
    de determinados pokemon. Se utiliza la libreria BeautifulSoup y requests
    para lograr la extraccion de informacion de la pagina web especificada"""

__author__ = "Brian Ezequiel Alaniz"
__email__ = "brian.alaniz@hotmail.com"

import requests
from bs4 import BeautifulSoup

HOST = 'https://pokemondb.net'
URL = '/pokedex/all'


"""Realiza la peticion al servidor y  Obtener su contenido"""

def get_content(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')
        return soup



"""Nos permite obtener la especie de un pokemon en especifico"""

def get_pokemon_species(url):
    soup = get_content(url)


    table = soup.find('table', class_='vitals-table')
    species = table.tbody.find_all('tr')[2].td.text

    return species


"""Nos permite mostrar por consola nombre,tipo,especie de cada pokemon"""

def show_pokemon_data():
    soup = get_content(HOST + URL)

    table = soup.find('table', {'id': 'pokedex'})

    for row in table.tbody.find_all('tr', limit=10):

        columns = row.find_all('td')

        name = columns[1].a.text
        type = [a.text for a in columns[2].find_all('a')]
        href = columns[1].a['href']

        next_url = HOST + href

        species = get_pokemon_species(next_url)
        print(name, *type, species)


if __name__ == '__main__':

   show_pokemon_data()
   