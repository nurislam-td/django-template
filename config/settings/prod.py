from .base import *  # noqa: F403
from .base import env

ADMIN_URL = env("DJANGO_ADMIN_URL")
SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = False
