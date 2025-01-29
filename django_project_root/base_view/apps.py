from django.apps import AppConfig


class BaseViewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_project_root.base_view'
