# Health Monitor API

This project was generated with [Django Admin] version 5.0
## Create Virtualenv
in cmd type `virtualalenv env`
Activate env using folowing command env\Script\Activate

## Install Dependencies

Navigate to the root directory of your project, where the requirements.txt file is located.
Run the command `pip3 install -r requirements.txt` to install all dependencies.

## Setup .env file
Create .env file in working directory.
Add `OPENAI_KEY` in .env file with its value if you want better result

## Migrate and Create superuser
Run following command line by line
1) `python manage.py makemigrations`
2) `python manage.py migrate`
3) `python manage.py createsuperuser`

## Development server
Run `python manage.py runserver` for a dev server. Navigate to `http://127.0.0.1:8000/api/`

## Further help

To get more help on the [Django Docs](https://docs.djangoproject.com/en/5.0/) page.
