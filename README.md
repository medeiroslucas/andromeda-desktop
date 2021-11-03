# Andromeda

## Utilização

Uma vez que as pipelines de deploy contínuo geram automativamente os arquivos executáveis a instalação consistem em baixar o arquivo zip associado a
versão desejada na lista de [releases](https://github.com/medeiroslucas/andromeda-desktop/releases) ([última versão](https://github.com/medeiroslucas/andromeda-desktop/releases/latest)). Após realizar o download deve-se descompactar o arquivo, essa operação resultara em uma pasta no formato andromeda_vX.Y.Z. Usando um terminal entre nesta pasta e modifique a permissão do arquivo executável com o comando `chmod +x andromeda`, após esta modificação basta executar o comando
`./andromeda`.

## Instalação para desenvolvimento

A utilização de containers docker no desenvovimento da aplicação facilitam a configuração de um ambiente unificado, sendo assim, para iniciar o desenvolvimento
é necessário buildar a aplicação com o seguinte comando:

`docker-compose build`

Após a execução do comando um container com o nome `andromeda-desktop_gui` será criado.

Uma das consequências de se utilizar uma biblioteca de GUI dentro do docker é a necessidade de executar comando especiais para que seja possível renderizar
com sucesso a interface, sendo assim, o comando para execusão do programa não segue o padrão do docker-compose, mas sim o seguinte comando:

``` bash
docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v $(pwd)/:/home/ -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v $(pwd)/app:/app --rm andromeda-desktop_gui
```

## Testes

A ferramenta selecionada para a construção dos testes unitários foi a biblioteca Pytest, sendo assim,
para executar os testes da aplicação basta executar seguinte comando no terminal:

`docker-compose run gui pytest`

Já para os testes de integração uma abordagem diferente foi selecionada. Uma vez que o usuário testando 
a aplicação pode não ter acesso a um dispositivo bluetooth BLE para realizar os testes de integração foi
desenvolvido um mock para a ESP32, tal mock escreve em dados que seriam enviados via bluetooth na saída
padrão da aplição, sendo assim, ao executar o aplicativo via terminal com o comando:

`./andromeda`

é possível acompanhar a escrita das coordenadas em tempo real durante a execução do aplicativo.

## Deploy

Com a finalidade de criar um fluxo automático de deploy e estar alinhado com as tendências de CI/CD de
desenvolvida uma pipelina de deploy contínuo baseado em tags nas branches `main` e `devel`. As tags geradas
na branch `devel` devem seguir o padrão `vX.Y.Z-dev.A` e representam o ambiente de staging da aplicação,
já as tags criadas na branch `main` devel seguir o padrão de `vX.Y.Z` e representam o ambiente de production da aplicação.

Em ambos os casos ao gerar uma nova tag uma action Action é disparada usando GitHub Actions, dentro dessa
action são executados os testes unitários e em caso de sucesso são executados os passos de `build` e `deploy`.
No passo de `build` é gerada uma imagem docker para a versão em questão que posteriomente é enviada para o
[registry do próprio repositório](https://github.com/medeiroslucas/andromeda-desktop/packages/1076733).
E por fim no passo de `deploy` é gerado um executável da aplicação utilizando a biblioteca `pyintaller`,
esse executável é compactado e enviado como um `asset` da release ficando disponível para download.
