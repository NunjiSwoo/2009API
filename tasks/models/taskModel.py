from django.db import models
from tasks.models.disciplineModel import DisciplineModel
from tasks.models.studentModel import StudentModel

class TaskModel(models.Model):
    titulo = models.CharField(max_length=40)
    description = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField()
    disciplines = models.ManyToManyField('DisciplineModel', related_name='Task_Disciplines')
    student = models.ForeignKey('StudentModel', on_delete=models.CASCADE)
