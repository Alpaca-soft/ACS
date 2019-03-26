# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Живая база
DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testACS',
        'USER': 'postgres',
        'PASSWORD': 'postgresdb',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
"""
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
