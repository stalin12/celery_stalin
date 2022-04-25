from __future__ import absolute_import
from celery import Celery

app = Celery('celery_stalin',
             backend='db+sqlite:///db.sqlite3',
             broker='amqp://stalin:stalin123@localhost/stalin_vhost',
             include=['celery_stalin.tasks'])

