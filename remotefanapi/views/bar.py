from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from remotefanapi.models import Bar, City, Team


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
        team_id = request.query_params.get("team")
        if team_id is not None:
            team = Team.objects.get(pk=team_id)
            for bar in bars:
                bar.joined = team in bar.teams.all()
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

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        bar = Bar.objects.get(pk=pk)
        bar.address = request.data["address"]
        owner = User.objects.get(pk=request.auth.user.id)
        bar.owner = owner
        city = City.objects.get(pk=request.data["city"])
        bar.city = city
        bar.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post', 'put'], detail=True)
    def edit_teams_in_bar(self, request, pk):
        """Custom action to add or remove teams from a bar"""
        try:
            team_ids = request.data["teams"]
            if not team_ids:
                return Response({"message": "Team IDs are missing"}, status=status.HTTP_400_BAD_REQUEST)

            teams = Team.objects.filter(pk__in=team_ids)
            bar = Bar.objects.get(pk=pk)

            if request.method == 'POST':
                bar.teams.add(*teams)
                return Response({'message': 'Teams added'}, status=status.HTTP_201_CREATED)
            elif request.method == 'PUT':
                bar.teams.clear()
                bar.teams.add(*teams)
                return Response({'message': 'Teams edited'}, status=status.HTTP_204_NO_CONTENT)
        except Bar.DoesNotExist:
            return Response({"message": "Bar not found"}, status=status.HTTP_404_NOT_FOUND)

class BarSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Bar
        fields = ('id', 'name', 'city', 'address', 'teams', 'owner')

