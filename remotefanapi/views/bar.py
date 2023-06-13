from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from remotefanapi.models import Bar, City


class BarView(ViewSet):
    """RemoteFan bar view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single bar

        Returns:
            Response -- JSON serialized bar
        """
        bar = Bar.objects.get(pk=pk)
        serializer = BarSerializer(bar)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all bars

        Returns:
            Response -- JSON serialized list of bars
        """
        bars = Bar.objects.all()
        serializer = BarSerializer(bars, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized bar instance
        """
        city=City.objects.get(pk=request.data["city"])
        owner=User.objects.get(pk=request.auth.user.id)
        bar = Bar.objects.create(
            name = request.data["name"],
            city = city,
            address = request.data["address"],
            owner = owner
        )
        serializer = BarSerializer(bar)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        bar = Bar.objects.get(pk=pk)
        bar.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class BarSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Bar
        fields = ('id', 'name', 'city', 'owner', 'teams')
