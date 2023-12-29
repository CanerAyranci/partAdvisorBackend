from django.http import JsonResponse, HttpResponse
from .models import Tire, Vehicle
from .serializers import TireSerializer, VehicleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def homePage(request):
    return HttpResponse('<h1> Server is online </h1> <br/>  <h3>Main host: http://127.0.0.1:8000</h3> <br/> <h3>Page: Main</h3> </br> <h3>Subs:</h3> Add "/api" to url to access api page. <br/>')

def apiPage(request):
    return HttpResponse('<h1> Server is online </h1> <br/>  <h3>Main host: http://127.0.0.1:8000</h3> <br/> <h3>Page: Api subpage</h3> <br/> <h3>Subs:</h3> Add "/vehicles" to url for Vehicle database. <br/> Add "/tires" to url for Tire database. <br/> <h3>Instructions:</h3> Add necesarry tags to access desired DB, "tag/id" lets you access to a spesific element of the table. <br/> Add ".json" end of the url to convert page into json file.')



@api_view(['GET', 'POST'])
def tireList(request, format=None):

    if request.method == 'GET':
        tires = Tire.objects.all()
        serializer = TireSerializer(tires, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TireSerializer(data = request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def tireDetail(request, id, format=None):

    try:
        tires = Tire.objects.get(pk=id)
    except Tire.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TireSerializer(tires)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TireSerializer(tires, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tires.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def vehicleList(request, format=None):

    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = VehicleSerializer(data = request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def vehicleDetail(request, model_id, format=None):

    try:
        vehicles = Vehicle.objects.get(pk=model_id)
    except Vehicle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VehicleSerializer(vehicles)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VehicleSerializer(vehicles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        vehicles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)