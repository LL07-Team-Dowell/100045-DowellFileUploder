from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'folder')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video', 'folder')