from .base import *

# DEBUG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env('ALLOWED_HOSTS')
