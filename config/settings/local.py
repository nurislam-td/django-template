from .base import *  # noqa: F403
from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

INSTALLED_APPS.extend(
    [
        "django_extensions",
        "debug_toolbar",
    ]
)

MIDDLEWARE.extend(
    [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
)
INTERNAL_IPS = [
    "127.0.0.1",
]
