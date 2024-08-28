# from __future__ import absolute_import, unicode_literals
# import os
# from celery import celery
#
# # Set the default Django settings module for the 'my_celery_app' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryProject.settings')
#
# # Create a Celery instance with the project's name
# app = celery('celeryProject')
#
# # Load task modules from all registered Django app configs.
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()