from local import *

DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'TESTS',
        'USER': 'postgresql',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}