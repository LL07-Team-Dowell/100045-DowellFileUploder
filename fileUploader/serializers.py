from rest_framework import serializers
from .models import *
import os
from django.conf import settings
import base64
from io import BytesIO
#New libraries to install
from PIL import Image



def read_file(folder, data):
    zip_file = data
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, zip_file.name)
    with open(file_path, 'wb') as f:
        f.write(zip_file.read())
    return os.path.relpath(file_path, settings.MEDIA_ROOT)
def read_file_image_video(folder, data, is_base64=False, name=""):
    # logger.debug("Harmless debug Message 88")
    zip_file = data
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    if is_base64:
        file_path = os.path.join(folder, name)
        with open(file_path, 'wb') as f:
            f.write(zip_file)
    else:
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
class QrCodeUpdateFileSerializer(serializers.Serializer):
    file = serializers.FileField()

class SecureRepoFileSerializer(serializers.Serializer):
    
    file = serializers.FileField()
    def create(self, validated_data): 
        return read_file(
            settings.SECURE_REP0_MEDIA_ROOT, 
            validated_data['file']
        )           

class AnnouncementFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    def create(self, validated_data): 
        return read_file(
            settings.ANNOUNCEMENT_MEDIA_ROOT, 
            validated_data['file']
        ) 
    
class CamVideosFileSerializer(serializers.Serializer):
    video_data = serializers.CharField()
    name = serializers.CharField()

    def validate(self, attrs):
        # Decode the Base64-encoded video data
        video_data = attrs.get('video_data')
        if video_data:
            # Decode the Base64-encoded video data
            try:
                decoded_data = base64.b64decode(video_data)
            except base64.binascii.Error:
                raise serializers.ValidationError("Invalid Base64 data.")

        # Create a BytesIO object from the decoded data
        video_file = BytesIO(decoded_data)
        return attrs

    def create(self, validated_data):    
        decoded_data = base64.b64decode(validated_data.pop('video_data'))
        name = validated_data.pop('name')
        return read_file_image_video(
                settings.CAM_COMPONENT_VIDEOS_MEDIA_ROOT, 
                # validated_data['file']
                decoded_data,
                True,
                name
            ) 
  
class CamImagesFileSerializer(serializers.Serializer):
    # file = serializers.FileField()
    image = serializers.ImageField()
    def validate_image(self, value):
        max_size = (2048, 2048)  # Maximum allowed size (width, height) in pixels

        # Open the image using PIL/Pillow
        image = Image.open(value)
        width, height = image.size

        # Perform size validation
        if width > max_size[0] or height > max_size[1]:
            raise serializers.ValidationError(
                f"Image dimensions should not exceed {max_size[0]}x{max_size[1]} pixels."
            )

        return value
    
    def create(self, validated_data):    
        return read_file_image_video(
            settings.CAM_COMPONENT_IMAGES_MEDIA_ROOT, 
            # validated_data['file']
            validated_data.pop('image')
        )   