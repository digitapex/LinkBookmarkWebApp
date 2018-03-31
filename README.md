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

Provide the SECRET_KEY in the secrets.py file, in the same folder as settings.py (the secrets.py.template file is provided for this purpose).

### Database choice

If you want to use SQLite, change the database section in settings.py to look like this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

If you instead want to use MySQL or PostgreSQL, change the above section appropriately and provide the database username and password in the above mentioned secrets.py file.

### Run the server

After chosing the database, run this in the topmost folder:

```
.manage.py makemigrations
.manage.py migrate
```

And finally, run the server:

```
.manage.py runserver
```

You can also chose the port:

```
.manage.py runserver 8080
```


