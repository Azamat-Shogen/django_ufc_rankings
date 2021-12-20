from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from athletes.models import Weightclass, Athlete
from athletes.serializers import WeightclassSerializer, AthleteSerializer
from rest_framework.decorators import api_view

# Create your views here.

# @csrf_exempt
@api_view(['GET', 'POST'])
def weightclasses_Api(request):
    if request.method == 'GET':
        weightclasses = Weightclass.objects.all()
        weightclasses_serializer = WeightclassSerializer(weightclasses, many=True)
        return JsonResponse(weightclasses_serializer.data, safe=False)

    elif request.method == 'POST':
        weightclass_data = JSONParser().parse(request)
        weightclasses_serializer = WeightclassSerializer(data=weightclass_data)
        if weightclasses_serializer.is_valid():
            weightclasses_serializer.save()
            return JsonResponse({"massage": "Weight class added successfully"}, safe=False)
        return JsonResponse({"massage": "Failed to add"}, safe=False)


# @csrf_exempt
@api_view(['PUT', 'GET', 'DELETE'])
def weight_class_detail(request, pk):
    try:
        weightclass = Weightclass.objects.get(pk=pk)
    except Weightclass.DoesNotExist:
        return JsonResponse({'message': 'Weight class does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        weightclass_serializer = WeightclassSerializer(weightclass)
        return JsonResponse(weightclass_serializer.data)
    
    elif request.method == 'PUT':
        weightclass_data = JSONParser().parse(request)
        weightclass_serializer = WeightclassSerializer(weightclass, data=weightclass_data)
        if weightclass_serializer.is_valid():
            weightclass_serializer.save()
            return JsonResponse(weightclass_serializer.data)
        return JsonResponse(weightclass_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        weightclass.delete()
        return JsonResponse({'message': 'Weight class deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)