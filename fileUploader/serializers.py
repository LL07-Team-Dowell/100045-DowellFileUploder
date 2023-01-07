from rest_framework import serializers
from .models import *
import zipfile
import os

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

    def create(self, validated_data):
        # Save the zip file to the specified folder
        zip_file = validated_data['file']
        folder = "./UploadedFiles"
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(os.path.join(folder, zip_file.name), 'wb') as f:
            f.write(zip_file.read())
        return validated_data