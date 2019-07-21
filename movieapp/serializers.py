from movieapp.models import *
from rest_framework.serializers import ModelSerializer

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DirectorSerializer(ModelSerializer):
    class Meta:
        model =Country
        fields = '__all__'

class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

