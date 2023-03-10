"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
from dotenv import load_dotenv
import os
from django.core.wsgi import get_wsgi_application

load_dotenv()

user_name = os.environ.get("USER")
password = os.environ.get("PASSWORD")

print(user_name, password)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
