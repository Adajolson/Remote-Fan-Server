from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from remotefanapi.models import Bar


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

class BarSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Bar
        fields = ('id', 'name', 'city', 'owner', 'teams')
