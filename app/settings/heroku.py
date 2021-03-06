import environ

from app.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DISABLE_COLLECTSTATIC=1

DATABASES = {
    "default": env.db(),
}
