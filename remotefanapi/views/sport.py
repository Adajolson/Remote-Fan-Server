from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from remotefanapi.models import Sport


class SportView(ViewSet):
    """RemoteFan sport view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single sport

        Returns:
            Response -- JSON serialized sport
        """
        try:
            sport = Sport.objects.get(pk=pk)
            serializer = SportSerializer(sport)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all sports

        Returns:
            Response -- JSON serialized list of sports
        """
        sports = Sport.objects.all()
        serializer = SportSerializer(sports, many=True)
        return Response(serializer.data)

class SportSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Sport
        fields = ('id', 'label')
