

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'Laboratory.deployment' if 'hostname' in os.environ else 'Laboratory.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
