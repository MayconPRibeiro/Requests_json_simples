#🍽️ Consulta de Restaurantes via API

Este é um script Python simples que consome uma API pública para retornar uma lista de restaurantes em formato JSON.

#📋 Descrição
O script utiliza a biblioteca requests para fazer uma requisição HTTP para a seguinte URL:

arduino
Copiar
Editar
https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json
Se a resposta da requisição for bem-sucedida (código 200), os dados JSON dos restaurantes são exibidos no terminal. Caso contrário, é exibida uma mensagem de erro com o código de status HTTP.

#💻 Requisitos
Python 3.6 ou superior

Biblioteca requests (pode ser instalada com pip)

#🚀 Como executar
Clone este repositório ou copie o script para sua máquina.

Instale as dependências (caso ainda não tenha a biblioteca requests):

bash
Copiar
Editar
pip install requests
Execute o script:

bash
Copiar
Editar
python nome_do_arquivo.py
#🧪 Exemplo de Saída
json
Copiar
Editar
[
  {
    "nome": "Restaurante Exemplo",
    "endereco": "Rua Exemplo, 123",
    "especialidade": "Comida Brasileira"
  },
  ...
]
#❗ Tratamento de Erros
Se a API estiver fora do ar ou a URL estiver incorreta, o script exibirá uma mensagem de erro semelhante a:

Copiar
Editar
Ops.. Status de Erro:404
#📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar!
