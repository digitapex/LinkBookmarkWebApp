# Links Bookmarks Web App

## Local installation

It's recommended to use the virtual environment for the installation.

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

Then provide the SECRET_KEY in the *secrets.py* file, which needs to be in the same folder as *settings.py* (the *secrets.py.template* file is provided for this purpose).

### Database choice

If you want to use SQLite, change the database section in *settings.py* to look like this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

If you instead want to use MySQL or PostgreSQL, change this section appropriately. The database username and password should be provided in the above mentioned *secrets.py* file.

### Run the server

After choosing the database, run this in the LinkBookmarkWebApp folder to create the necessary database tables:

```
./manage.py migrate
```

Finally, run the server:

```
./manage.py runserver
```

Now go to <http://localhost:8000/> to view the app.


