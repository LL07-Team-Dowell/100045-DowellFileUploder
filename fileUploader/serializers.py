from rest_framework import serializers
from .models import *
import os
from django.conf import settings
#New libraries to install
from moviepy.editor import VideoFileClip
from PIL import Image


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

class AnnouncementFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    def create(self, validated_data): 
        return read_file(
            settings.ANNOUNCEMENT_MEDIA_ROOT, 
            validated_data['file']
        ) 
    
class CamVideosFileSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_video(self, value):
        video = value.file.name
        clip = VideoFileClip(video)
        duration = clip.duration
        clip.close()
        if duration > 60:  # Duration is in seconds
            raise serializers.ValidationError("Video duration should not exceed 1 minute.")
        return value

    
    def create(self, validated_data):    
        return read_file(
            settings.CAM_COMPONENT_VIDEOS_MEDIA_ROOT, 
            # validated_data['file']
            validated_data.pop('video')

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
        return read_file(
            settings.CAM_COMPONENT_IMAGES_MEDIA_ROOT, 
            # validated_data['file']
            validated_data.pop('image')
        )   