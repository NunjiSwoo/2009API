Para rodar o código basta apenas rodar o comando: 
python -m venv .env
Ativar esta mesma:
.\.env\Scripts\activate
Realizar as migrações:
python manage.py makemigrations
python manage.py migrate
E por ultimo:
python manage.py runserver
