django-admin startproject mydemo

.\mydemo>python manage.py startapp myapp

# Create the database and migrate

python manage.py makemigrations
python manage.py migrate

python manage.py runserver --verbosity=2

python manage.py createsuperuser