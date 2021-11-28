from django.db import models


class LogMeu(models.Model):
    nome = models.CharField(max_length=100, default='Nome')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
