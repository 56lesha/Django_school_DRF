from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from school.models import Student
from school.serializers import StudentSerializer


# Create your views here.title

class StudentViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#with generics

# class StudentListAPIView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



#with APIView
# class StudentAPIView(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         return Response({"students": StudentSerializer(students, many=True).data})
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() #автоматически вызывает метод create
#         return Response({"new_student": serializer.data})
#
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None) # получаем по ключу из пришедшего словаря kwargs pk или возвращаем None
#         if not pk:
#             return Response({"error": "I don't know what to update"})
#
#         try:
#             instance = Student.objects.get(pk=pk)
#         except:
#             return Response({"error": "Instance doesn't exists"})
#
#         serializer = StudentSerializer(instance=instance, data=request.data) #передаём данные в сереализатор, чтобы обработать их и получить данные, которые подходят для модели Student
#         serializer.is_valid() # проверяет данные и создаёт переменную validated_data
#         serializer.save() # вызывает метод update в сериализаторе
#         return Response({"updated": serializer.data})
#
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "I don't know what to update"})
#
#         try:
#             instance = Student.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Instance doesn't exists"})
#
#
#         return Response({"post": f"Objects {str(pk)} is deleted" })








































