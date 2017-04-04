from base import *


DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'ssms_db',
        'USER': 'ssms_user',
        'PASSWORD': 'ssms_pass',
    }
}
