import dj_database_url
from .settings import *

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.postgresql_psycopg2',
#            'NAME': 'd3to0s3cnveo0',
#            'USER': 'vohcmomsthnsaa',
#            'PASSWORD': 'abd7b8e0fef2201417566e2e5331824985ae465099e7dbb2700a045fa668d96b',
#            'HOST': 'ec2-3-219-52-220.compute-1.amazonaws.com',
#            'PORT': 5432,
#        }
# }
