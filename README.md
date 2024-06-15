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

## Output
![Screenshot 2024-06-15 124812](https://github.com/amitgit712/health-monitor-api/assets/67471434/bd42bcdb-fd39-4352-b6b1-fac64dc472de)

![Screenshot 2024-06-15 125012](https://github.com/amitgit712/health-monitor-api/assets/67471434/cf1c7883-8e40-4be8-a122-da16e2ec68f5)

## Further help

To get more help on the [Django Docs](https://docs.djangoproject.com/en/5.0/) page.
