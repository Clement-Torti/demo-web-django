from django.shortcuts import render, redirect
from .models import Client
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers import serialize


# Create your views here.
def getClients(request):
    data = Client.objects.all()
        # Serialize the data to a JSON format
    client_list = []
    for client in data:
        client_data = {
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'age': client.age,
            'gender': client.gender,
        }
        client_list.append(client_data)

    # Create a dictionary containing the serialized data
    response_data = {"data": client_list}

    return JsonResponse(response_data, status=200)


@csrf_exempt
def insertClient(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # Now you can access the data as a Python dictionary
        name = data['name']
        email = data['email']
        age = data['age']
        gender = data['gender']
        
        print(name, email, age, gender)

        query = Client(name=name, email=email, age=age, gender=gender)
        query.save()

        return JsonResponse({'message': 'Data inserted successfully'}, status=201)
        
    return JsonResponse({'message': '/insert should be a POST method providing json client'})


@csrf_exempt
def updateClient(request, id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # Now you can access the data as a Python dictionary
        name = data['name']
        email = data['email']
        age = data['age']
        gender = data['gender']
        
        print(name, email, age, gender)

        query = Client(id=id, name=name, email=email, age=age, gender=gender)
        query.save()

        return JsonResponse({'message': 'Data updated successfully'}, status=200)
        

    return JsonResponse({'message': '/update/<id> should be a POST method providing json client'})


def deleteClient(request, id):
    d = Client.objects.get(id=id)
    d.delete()
    
    return JsonResponse({'message' : 'client with id ${id} deleted successfully'}, status=202)