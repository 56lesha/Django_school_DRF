import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from school.models import Student, Group


class StudentSerializer(serializers.ModelSerializer): # сериализатор для перевода данных во внутренний тип данных Python - словарь
    class Meta:
        model = Student
        fields = '__all__'









    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)

    # Например, если `validated_data` имеет вид:
    # ```
    # {
    #     'name': 'John',
    #     'age': 20,
    #     'major': 'Computer Science'
    # }
    # ```
    # То вызов метода `Student.objects.create(**validated_data)` будет эквивалентен
    # вызову: Student.objects.create(name='John', age=20, major='Computer Science')

    # def update(self, instance, validated_data):
    #     instance.firstname = validated_data.get('firstname', instance.firstname)
    #     instance.lastname = validated_data.get('lastname', instance.lastname)
    #     instance.group_id = validated_data.get('group_id', instance.group_id)
    #     instance.save()
    #     return instance

































#Proccess of serializer
# class Student:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
# def encode():
#     student = Student("Alexey", "Romanyuk") # создали объект класса для перевода
#     student_sr = StudentSerializer(student) # перевели данные в словарь
#     print(student_sr.data)
#     print(type(student_sr.data))
#     json = JSONRenderer().render(student_sr.data) # переводим данные в JSON
#     print(json)
#     print(type(json))
#
#
#
#
# def decode():
#     json = b'{"firstname":"Alexey","lastname":"Romanyuk"}'
#     stream = io.BytesIO(json) #создаём объект BytesIO, который представляет собой буфер в памяти для работы с данными в виде байтов
#     print(f"STREAM - {stream}")
#     data = JSONParser().parse(stream) # переводим данные в нативные типы данных Python
#     print(f"DATA - {data}")
#     serializer = StudentSerializer(data=data) # переводим нативные типы данных  в словарь проверенных данных
#     print(f"SERIALIZER - {serializer}")
#     serializer.is_valid()
#     print(f"SERIALIZER.VALIDATED_DATA {serializer.validated_data}")




