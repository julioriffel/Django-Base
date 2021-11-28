#  Copyright (c) 2021.
#  Julio Cezar Riffel<julioriffel@gmail.com>

from .celery import app as celery_app

__all__ = ('celery_app',)
