import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Backends disponibles : 'postgresql', 'mysql', 'sqlite3' et 'oracle'.
        'NAME': 'Airlines_db',             # Nom de la base de données
        'USER': 'Air_UserADM',
        'PASSWORD': '819bbe731f328d9b15873627e7b5c5dd',        
        'HOST': 'localhost',                    # Utile si votre base de données est sur une autre machine
        'PORT': '3306',                         # ... et si elle utilise un autre port que celui par défaut
    }
}

# Langage utilisé au sein de Django, pour afficher les messages d'information et d'erreurs notamment
LANGUAGE_CODE = 'fr-FR'
# Fuseau horaire, pour l'enregistrement et l'affichage des dates
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]