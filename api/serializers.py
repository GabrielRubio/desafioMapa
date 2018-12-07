from rest_framework import serializers
from .models import Maps, Distances

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maps
        fields = '__all__'

class DistancesSerializer(serializers.ModelSerializer):
    map_name = serializers.SerializerMethodField('maps_serializer')

    def maps_serializer(self):
        map_name = Maps.objects.filter(maps_id = self.id)
        return map_name
        
    class Meta:
        model = Distances
        # fields = ('map_name', 'point_A','point_B','distance')
        fields = ('__all__')


