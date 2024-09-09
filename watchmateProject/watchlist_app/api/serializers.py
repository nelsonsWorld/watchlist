from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform
from rest_framework.validators import UniqueValidator



class WatchListSerializer(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField() #Look up Serializer Method Field

    class Meta:
        model = WatchList
        # fields = ['id', 'account_name', 'users', 'create'] # Just an example of how the fields can be carried
        fields = "__all__"
        # exclude = ['active'] #you can only use this variable without the other 'fields' variable
        
    def get_len_name(self, object):
        return len(object.title)
        ## This way is the same as the above, just elongated
        # length = len(object.name)
        # return length
 
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different!")
        else:
            return data
        
    
        
    def validate_name(self,value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value
        
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) #many=True allows you to have (fill in)
    # watchlist = serializers.StringRelatedField(many=True) #This will display all the string fields and take out any other content like pk (primary key)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # This will display pk field only
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"