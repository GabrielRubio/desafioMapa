# from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Maps, Distances
from .serializers import DistancesSerializer

import networkx as nx

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


@csrf_exempt
def shorterDistance(request):
    """
    Finding the smallest path and cost.
    Method: POST
    Content type: application/json
    Body exemplo: {
                        "mapName": "SP",
                        "start": "A",
                        "end": "D",
                        "autonomy": 10,
                        "liters": 2.50
                    }
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        id_map = Maps.objects.get(name=data.get('mapName'))
        list_distance = Distances.objects.get(map_name=id_map)
        
        # creating the graph
        G=nx.Graph()
        for dist in list_distance:
            G.add_edge(dist.start,dist.end,weight=dist.distance)
        
        # finding shortest path and the length
        path = nx.shortest_path(G, data.get('start'), data.get('end'))
        path_length = 0
        for i in range(0,len(path)):
            a = path[i]
            b = path[i+1]
            path_length += G[a][b]['weight']

        # Calculating costs
        autonomy = data.get('autonomy')
        litersCost = data.get('liters')
        costs = (path_length * litersCost) / autonomy

        result = {'path': path, 'cost':costs}

        return JsonResponse(result, status=200)

