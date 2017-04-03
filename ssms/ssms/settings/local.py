from base import *


DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': os.environ.get('SSMS_DATABASE_NAME', 'ssms_db'),
        'USER': os.environ.get('SSMS_DATABASE_USER', 'ssms_user'),
        'PASSWORD': os.environ.get('SSMS_DATABASE_PASS', 'ssms_pass'),
        'HOST': os.environ.get('SSMS_DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('SSMS_DATABASE_PORT', '5432'),
    }
}

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)

INSTALLED_APPS += ['django_extensions', ]

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}
