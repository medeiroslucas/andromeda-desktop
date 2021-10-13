# Andromeda

## Instalação

A instalação do ambiente de desenvolvimento da aplicação Andromeda é dividida em duas partes,
a instalação de dependências python realizada via Poetry, e a instalação das dependências associadas 
a utilização da biblioteca de Bluetooth BLE

### Bluetooth BLE

A utilização da biblioteca `gattlib` além do pacote python também depende de outras bibliotecas
instaladas diretamente via apt (se tratando de ambiente debian). Siga o manual de instalação pelo 
[link](https://github.com/oscaracena/pygattlib)

### Dependências Python

O gerenciador de dependências selecionado para o projeto foi o Poetry, sendo assim o primeiro passo
é instala-lo (recomenda-se a utilização de um ambiente virtual para instalação):

`pip install poetry`

Logo em seguida devemos executar o comando:

`poetry install`

Após a execução as dependências python estarão prontas para utilização

## Utilização

A utilização do projeto pode ser feita ao executarmos o arquivo `main.py` com o seguinte comando:

`python3 main.py`

Ao executar esse comando uma interface será aberta e o fluxo principal não necessita de execuções de
comandos no terminal

## Testes

A ferramenta selecionada para a construção dos testes unitários foi a biblioteca Pytest, sendo assim,
para executar os testes da aplicação basta executar seguinte comando no terminal:

`pytest`

Já para os testes de integração uma abordagem diferente foi selecionada. Uma vez que o usuário testando 
a aplicação pode não ter acesso a um dispositivo bluetooth BLE para realizar os testes de integração foi
desenvolvido um mock para a ESP32, tal mock escreve em dados que seriam enviados via bluetooth em um
arquivo chamado `mock_coords.txt`, sendo assim, com o comando:

`tail -f mock_coords.txt`

é possível acompanhar a escrita das coordenadas em tempo real durante a execução do aplicativo.