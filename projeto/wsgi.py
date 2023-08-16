"""
WSGI config for projeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")

DjangoInstrumentor().instrument()
Psycopg2Instrumentor().instrument()

application = get_wsgi_application()
