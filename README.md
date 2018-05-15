# Links Bookmarks Web App

Available online at <https://petebill.pythonanywhere.com/>
Also available at <https://linksbookmarks.herokuapp.com/>

## Local installation

Perform these steps to create and activate the virtual environment, clone this repository and install the dependecies:

```
mkdir your_folder_name
cd your_folder_name
virtualenv vEnv
source vEnv/bin/activate
git clone https://github.com/digitapex/LinkBookmarkWebApp.git
cd LinkBookmarkWebApp
pip install -r requirements.txt
```

Then in the *settings.py* file change these two lines:

1. Change the secret key by changing *default_key* to your secret key

```
SECRET_KEY = os.environ.get('SECRET_KEY', 'default_key')
```

2. Change the postgres_username, postgres_password and database_name to correspond to your local PostgreSQL installation (or alternativly use SQLite):

```
DATABASES = { 'default': dj_database_url.config(default='postgres://postgres_user:postgres_password@localhost:5432/database_name') }
```

After that run:

```
./manage.py migrate
./manage.py runserver
```

Finally go to <http://localhost:8000/> to view the app.
