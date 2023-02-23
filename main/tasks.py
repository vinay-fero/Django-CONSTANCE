from django_constance.celery import celery_app
from constance import config


@celery_app.task()
def constance_test():
    print_value = config.THE_ANSWER_CONFIG
    print("print_value", print_value)
