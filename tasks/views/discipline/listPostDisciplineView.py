from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models.disciplineModel import DisciplineModel
from tasks.serializers.disciplineSerializer import DisciplineSerializer

class ListPostDisciplineView(APIView):
    def get(self, request):
        discipline = DisciplineModel.objects.all()
        serializer = DisciplineSerializer(discipline, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DisciplineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)