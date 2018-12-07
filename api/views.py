# from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Maps, Distances
from .serializers import DistancesSerializer

@csrf_exempt
def saveMap(request):
    """
    Saving distances of points in the city.
    Method: POST
    Content type: application/json
    Body exemplo: {
                        "mapName": "SP",
                        "route": [
                            ["A","B",10],
                            ["B","D",15],
                            ["C","E",24],
                            ["E","F",1]
                        ]   
                    }
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        fields = ['point_A','point_B','distance']
        data2 = [dict(zip(fields, route)) for route in data.get('route')]
        print(data2)
        
        serializerMap = DistancesSerializer(data=data2, many=True)
        if serializerMap.is_valid():
            serializerMap.save()
            return JsonResponse(serializerMap.data, status=201)
        return JsonResponse(serializerMap.errors, status=400)

