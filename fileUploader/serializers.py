from rest_framework import serializers
from .models import *
import os
from django.conf import settings


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

    def create(self, validated_data):            
        zip_file = self.validated_data['file']
        folder = settings.MEDIA_ROOT
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = os.path.join(folder, zip_file.name)
        with open(file_path, 'wb') as f:
            f.write(zip_file.read())
        return zip_file.name