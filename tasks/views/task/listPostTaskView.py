from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models.taskModel import TaskModel
from tasks.serializers.taskSerializer import TaskSerializer

class ListPostTaskView(APIView):
    def get(self, request):
        task = TaskModel.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)