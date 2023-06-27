from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import os
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class ImageUploadView(APIView):
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            folder = serializer.validated_data['folder']
            folder_path = os.path.join(settings.MEDIA_ROOT, folder)
            os.makedirs(folder_path, exist_ok=True)
            image_path = os.path.join(folder_path, image.name)
            with open(image_path, 'wb') as file:
                file.write(image.read())
            domain = get_current_site(request).domain
            public_link = f"http://{domain}{os.path.join(settings.MEDIA_URL, folder, image.name)}"

            return Response({'public_link': public_link}, status=201)
        else:
            return Response(serializer.errors, status=400)
        
@method_decorator(csrf_exempt, name='dispatch')
class VideoUploadView(APIView):
    def post(self, request, format=None):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            video = serializer.validated_data['video']
            folder = serializer.validated_data['folder']

            # Create the folder if it doesn't exist
            folder_path = os.path.join(settings.MEDIA_ROOT, folder)
            os.makedirs(folder_path, exist_ok=True)

            # Save the video to the specified folder
            video_path = os.path.join(folder_path, video.name)
            with open(video_path, 'wb') as file:
                file.write(video.read())

            # Get the public link to the uploaded video with the full URL
            domain = get_current_site(request).domain
            video_link = f"http://{domain}{os.path.join(settings.MEDIA_URL, folder, video.name)}"

            return Response({'video_link': video_link}, status=201)
        else:
            return Response(serializer.errors, status=400)