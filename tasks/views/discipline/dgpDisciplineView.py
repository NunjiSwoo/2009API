from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models.disciplineModel import DisciplineModel
from tasks.serializers.disciplineSerializer import DisciplineSerializer

class DGPDisciplineView(APIView):
    def delete(self, request, discipline_id):
        try:
            discipline = DisciplineModel.objects.get(pk=discipline_id)
        except DisciplineModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        discipline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, discipline_id):
        try:
            discipline = DisciplineModel.objects.get(pk=discipline_id)
        except DisciplineModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DisciplineSerializer(discipline)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, discipline_id):
        try:
            discipline = DisciplineModel.objects.get(pk=discipline_id)
        except DisciplineModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DisciplineSerializer(discipline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)