"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os,sys
from django.core.wsgi import get_wsgi_application
sys.path.append('r/opt/sysadmin')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
reload(sys)
sys.setdefaultencoding("utf-8")

application = get_wsgi_application()
