# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j4b)__-b(u&sa$fqi))i^a^tgr!n_nwbx%yhdro_0ndwkd@a(z'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Doghotman85!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}