"""
APPs interface for myapp.
"""
from django.apps import AppConfig


class MyappConfig(AppConfig):
    """
    class MyappConfig for myapp.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
