from rest_framework import serializers
from tasks.models.disciplineModel import DisciplineModel

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineModel
        fields = '__all__'