import os

import celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_constance.settings")

celery_app = celery.Celery("django_constance")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
