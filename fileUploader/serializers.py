from rest_framework import serializers
from .models import *
import os
from django.conf import settings
import mimetypes
from io import BytesIO
#New libraries to install
from PIL import Image



def read_file(folder, data, name=None):
    zip_file = data
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    if name:
        file_path = os.path.join(folder, name)
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

class DigitalQFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    def create(self, validated_data): 
        return read_file(
            settings.DIGITAL_QUEUE_MEDIA_ROOT, 
            validated_data['file']
        ) 
    
class CamVideosFileSerializer(serializers.Serializer):
    video = serializers.FileField()

    def is_video(self, filename):
        mime_type, _ = mimetypes.guess_type(filename)
        return mime_type is not None and mime_type.startswith('video/')
    
    def create(self, validated_data):  
        if not self.is_video(validated_data['video'].name):
            raise serializers.ValidationError({"error": 'The uploaded file is not a video. Please upload a video file.'})

        
        return read_file(
                settings.CAM_COMPONENT_VIDEOS_MEDIA_ROOT, 
                validated_data['video'],
            ) 

class CamImagesFileSerializer(serializers.Serializer):
    image = serializers.ImageField()
    
    def create(self, validated_data):    
        return read_file(
            settings.CAM_COMPONENT_IMAGES_MEDIA_ROOT, 
            validated_data.pop('image')
        )   
    
class PublicSecureRepoFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    def create(self, validated_data): 
        return read_file(
            settings.PUBLIC_SECURE_REP0_MEDIA_ROOT, 
            validated_data['file']
        )  
    

class HrImagesFileSerializer(serializers.Serializer):
    image = serializers.ImageField()
    
    def create(self, validated_data):    
        return read_file(
            settings.HR_MEDIA_ROOT, 
            validated_data.pop('image')
        ) 
    
class SamantaCampaignFileSerializer(serializers.Serializer):
    image = serializers.FileField()
    
    def create(self, validated_data):    
        return read_file(
            settings.SAMANTA_MEDIA_ROOT, 
            validated_data.pop('image')
        ) 
class MyFridgeFileSerializer(serializers.Serializer):
    image = serializers.FileField()
    
    def create(self, validated_data):    
        return read_file(
            settings.MYFRIDGE_MEDIA_ROOT,  
            validated_data.pop('image')
        ) 

class DowellCubesFileSerializer(serializers.Serializer):
    image = serializers.FileField()
    
    def create(self, validated_data):    
        return read_file(
            settings.DOWELLCUBES_MEDIA_ROOT,  
            validated_data.pop('image')
        ) 

class SavePdfFileSerializer(serializers.Serializer):
    pdf = serializers.FileField()

    def is_pdf(self, filename):
        mime_type, _ = mimetypes.guess_type(filename)
        if mime_type == 'application/pdf':
            return True
        else:
            return False

    def create(self, validated_data): 
        if not self.is_pdf(validated_data['pdf'].name):
            raise serializers.ValidationError({"error": 'The uploaded file is not an pdf. Please upload an pdf file.'})
        return read_file(
            settings.SAVE_PDF, 
            validated_data['pdf']
        )   
    

class VoiceRecordingFileSerializer(serializers.Serializer):
    audio = serializers.FileField()

    def is_audio(self, filename):
        mime_type, _ = mimetypes.guess_type(filename)
        return mime_type is not None and mime_type.startswith('audio/')
    
    def create(self, validated_data):  
        if not self.is_audio(validated_data['audio'].name):
            raise serializers.ValidationError({"error": 'The uploaded file is not an audio. Please upload an audio file.'})

        
        return read_file(
            settings.VOICE_RECORDING, 
            validated_data['audio'],
        ) 