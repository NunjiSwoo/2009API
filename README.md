## Projeto
Este projeto foi criado por mim, Renan Henrique de Oliveira, com a finalidade de ser entrege para os doscentes do SENAI São Gaspar Ricardo Jr. de forma que possa ser avaliado de acordo com critérios préviamente impostos.

O seu objetivo é de criar uma API na qual tera a função de cadastrar alunos, disciplinas e tarefas, correspondendo com as instruções fornecidas para os discentes.

## Instalação

Para executar este arquivo em sua maquina sera necessario primeiro ter django e uma IDE baixados, depois é necessario baixar ele de meu repositório GitHub, onde com apenas um comando:

git clone https://github.com/NunjiSwoo/2009API.git

Em um cmd aberto na pasta que desejar ira automaticamente instalar um arquivo em uma Pasta: "2009API"

neste mesmo cmd é possivel rodar o comando(Windows):

cd .\2009API\

code .

Para iniciar o projeto em seu Visual Studio Code, ou caso não use ele, apenas abra procurando esta pasta em sua IDE.

## Execução

Para começarmos a executar esta IDE é nescessario que voce crie um Virtual Environment com os comandos em seu cmd ou em seu terminal do VS Code:

python -m venv .env

.env\Scripts\activate

Em seguida baixe Django rest_framework com o comando:

pip install django-rest-framework

Agora estamos quase lá, rode os comandos:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Pronto, sua IDE ja esta rodando na porta http://127.0.0.1:8000, nela você podera ver endpoints(URLs) a serem seguidas, estas podem criar, atualizar, exibir e deletar dados, estes dados são locais e terão de ser enseridos manualmente, ou com a ajuda do meu arquivo postman parte disto ja esta pronto.
