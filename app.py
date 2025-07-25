import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}

    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "preco": item['price'],
            "descricao": item['description']
        })

    for nome_do_restaurante, dados in dados_restaurante.items():
        nome_do_arquivo = f'{nome_do_restaurante}.json'
        with open(nome_do_arquivo, 'w') as arquivo_restaurante:
            json.dump(dados, arquivo_restaurante, indent=4)

else:
    print(f'Ops.. Status de Erro:{response.status_code}')