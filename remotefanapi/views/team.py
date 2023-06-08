from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from remotefanapi.models import Team


class TeamView(ViewSet):
    """RemoteFan team view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single team

        Returns:
            Response -- JSON serialized team
        """
        try:
            team = Team.objects.get(pk=pk)
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all teams

        Returns:
            Response -- JSON serialized list of teams
        """
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class TeamSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Team
        fields = ('id', 'name', 'city', 'sport')
