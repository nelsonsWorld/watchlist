from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review
from rest_framework.validators import UniqueValidator


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
            model = Review
            exclude = ('watchlist',)
        #  fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList

        fields = "__all__"
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) 


    class Meta:
        model = StreamPlatform
        fields = "__all__"