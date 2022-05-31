#  Copyright (c) 2021.
#  Julio Cezar Riffel<julioriffel@gmail.com>
from celery import shared_task

from base.models import LogMeu


@shared_task(rate_limit='2/m')
def somar(x=0, y=0):
    return x + y


@shared_task(rate_limit='2/m')
def novo_log():
    LogMeu.objects.create(id=None)
