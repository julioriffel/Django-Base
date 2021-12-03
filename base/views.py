from celery import group
from django.http import HttpResponse

from base.tasks import fun_A


def a(request):
    # g = group(fun_A.s(), fun_B.s())
    g = group(fun_A.s() for i in range(96))
    res = g()

    return HttpResponse(f'Hello, world!{res.get()}')
