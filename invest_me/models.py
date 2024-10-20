from django.db import models
from datetime import datetime

"""
# Investimento
# Valor
# Pago
# Data

https://docs.djangoproject.com/pt-br/4.2/topics/db/models/
"""


class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    nivel = models.IntegerField(default=1)
