from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'author', 'title', 'isExplicit', 'image', 'lyrics', 'musicFile', 'dateCreated')

       