from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform
from rest_framework.validators import UniqueValidator



class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList

        fields = "__all__"
        
        
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) 


    class Meta:
        model = StreamPlatform
        fields = "__all__"