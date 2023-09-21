from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models.studentModel import StudentModel
from tasks.serializers.studentSerilizer import StudentSerializer

class DGPStudentView(APIView):
    def delete(self, request, student_id):
        try:
            student = StudentModel.objects.get(pk=student_id)
        except StudentModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, student_id):
        try:
            student = StudentModel.objects.get(pk=student_id)
        except StudentModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, student_id):
        try:
            student = StudentModel.objects.get(pk=student_id)
        except StudentModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)