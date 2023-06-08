from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from remotefanapi.models import City


class CityView(ViewSet):
    """RemoteFan city view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single city

        Returns:
            Response -- JSON serialized city
        """
        city = City.objects.get(pk=pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all cities

        Returns:
            Response -- JSON serialized list of cities
        """
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

class CitySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = City
        fields = ('id', 'name', 'state')
