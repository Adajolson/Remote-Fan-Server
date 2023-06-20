from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
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
    
    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized city instance
        """
        city = City.objects.create(
            name = request.data["name"],
            state =  request.data["state"]
        )
        serializer = CitySerializer(city)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        city = City.objects.get(pk=pk)
        city.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CitySerializer(serializers.ModelSerializer):
    """JSON serializer for cities
    """
    class Meta:
        model = City
        fields = ('id', 'name', 'state')
