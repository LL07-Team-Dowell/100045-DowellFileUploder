from rest_framework import serializers
from .models import *
import os
from django.conf import settings


def read_file(folder, data):
    zip_file = data
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, zip_file.name)
    with open(file_path, 'wb') as f:
        f.write(zip_file.read())
    return os.path.relpath(file_path, settings.MEDIA_ROOT)

class QrCodeFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    
    def create(self, validated_data):    
        return read_file(
            settings.QRCODE_MEDIA_ROOT, 
            validated_data['file']
        )        
class SecureRepoFileSerializer(serializers.Serializer):
    
    file = serializers.FileField()
    def create(self, validated_data): 
        return read_file(
            settings.SECURE_REP0_MEDIA_ROOT, 
            validated_data['file']
        )           
    