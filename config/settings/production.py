from .base import *
from .base import env

# DEBUG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DEBUG', default=False)

# SECRET CONFIG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key

# DATABASE CONFIG
# --------------------------------------------------------------------------------------
DATABASES["default"] = env.db("DATABASE_URL")


# STATIC CONFIG
# --------------------------------------------------------------------------------------
STATIC_ROOT = env("STATIC_ROOT")

# MEDIA CONFIG
# --------------------------------------------------------------------------------------
MEDIA_ROOT = env("MEDIA_ROOT")

# PASSWORD VALIDATORS
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
