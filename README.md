# Coral Framework

## Stack:

- Django framework
- Python 3.7
- jQuery
- HTML 5
- CSS 3
- Javascript


Por padrão o django está com o sqlite configurado como banco de dados. Até colocarmos o servidor no ar corretamente com o PostgreSQL. 


## Para executar o projeto, siga os seguintes passos:

`git clone git@github.com:rafaelescalfoni/coral.git`

Navegue até o diretório do projeto via linha de comando:

`cd /diretório até o projeto no seu pc/coral/`

Caso não tenha o Python3, instale-o utilizando o seguinte comando (mac):

`brew install python3`

Para rodar as migrações que constroem o banco de dados, execute o comando:

`python3.7 manage.py migrate`

ou

`python manage.py migrate`

Para dar start no django server utilize o comando:

`python3.7 manage.py runserver`

ou 

`python manage.py runserver`

Enjoy! ;)

## Diagrama do banco de dados

![Diagrama](coral_models.png)