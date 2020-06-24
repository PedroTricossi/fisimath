from django.db import models

from pages.models import Areas

class AreasEspecificas(models.Model):
    nome_area = models.ForeignKey(Areas, on_delete=models.CASCADE, related_name='name_area')

    nome_formula = models.CharField(max_length=200)

    formula = models.CharField(max_length=500)

    casos_uso = models.CharField(max_length=500, default='.')

    def __str__(self):
        return self.nome_formula