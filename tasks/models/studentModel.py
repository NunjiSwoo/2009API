from django.db import models

class StudentModel(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()