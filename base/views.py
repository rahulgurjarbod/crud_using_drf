from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Person
from . serializers import PersonSerializer


@api_view(['GET'])
def getPerson(request, pk):
    if request.method == 'GET':
        person = Person.objects.get(id=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def getAllPersons(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def createPerson(request):
    if request.method == 'POST':
        person = Person.objects.create(
            name=request.data["name"],
            rollNo=request.data["rollNo"],
            section=request.data["section"],
            phoneNo=request.data["phoneNo"],
            address=request.data["address"],
        )
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

@api_view(['PUT'])
def updatePerson(request, pk):
    if request.method == 'PUT':
        person = Person.objects.get(id=pk)
        serializer = PersonSerializer(instance=person, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

@api_view(['PATCH'])
def partialUpdate(request, pk):
    if request.method == 'PATCH':
        person = Person.objects.get(id=pk)
        serializer = PersonSerializer(instance=person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['DELETE'])
def deletePerson(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    return Response('Person Deleted !!')