from django.db import models

class DisciplineModel(models.Model):
    nome = models.CharField(max_length=30)
    description = models.TextField()