from rest_framework import serializers
from watchlist_app.models import Movie
from rest_framework.validators import UniqueValidator

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        # fields = ['id', 'account_name', 'users', 'create'] # Just an example of how the fields can be carried
        fields = "__all__"
        # exclude = ['active'] #you can only use this variable without the other 'fields' variable
        
 
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