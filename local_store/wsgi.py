"""
WSGI config for local store development.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'local_store.settings')

application = get_wsgi_application()
