from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models.taskModel import TaskModel
from tasks.serializers.taskSerializer import TaskSerializer

class DGPTaskView(APIView):
    def delete(self, request, task_id):
        try:
            task = TaskModel.objects.get(pk=task_id)
        except TaskModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, task_id):
        try:
            task = TaskModel.objects.get(pk=task_id)
        except TaskModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, task_id):
        try:
            task = TaskModel.objects.get(pk=task_id)
        except TaskModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)