"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import environ  # noqa
from django.core.wsgi import get_wsgi_application

environ.Env().read_env(".env")
application = get_wsgi_application()
