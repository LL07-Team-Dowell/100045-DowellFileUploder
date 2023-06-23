from django.conf import settings
from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

@method_decorator(csrf_exempt, name='dispatch')
class QrCodeUploadView(APIView):
    def post(self, request, format=None):
        serializer = QrCodeFileSerializer(data=request.data)
        if serializer.is_valid():
            file_path = serializer.save()
            file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)
            return Response({'file_url': file_url}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, file_name, format=None):
    #     serializer = QrCodeFileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         file_path = serializer.save()  # Save the file and get the file path
    #         new_file_path = f"{settings.QRCODE_MEDIA_ROOT}/{file_name}"  # Path to the new file you want to replace with
    #         with open(new_file_path, 'rb') as new_file:
    #             # Update the existing file with the new file data
    #             serializer.update(serializer.instance, {'file': new_file})
    #         file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)
    #         return Response({'file_url': file_url}, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class SecureRepoFileUploadView(APIView):
    def post(self, request, format=None):
        serializer = SecureRepoFileSerializer(data=request.data)
        if serializer.is_valid():
            file_path = serializer.save()
            file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)
            return Response({'file_url': file_url}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementFileUploadView(APIView):
    def post(self, request, format=None):
        serializer = AnnouncementFileSerializer(data=request.data)
        if serializer.is_valid():
            file_path = serializer.save()
            file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)
            return Response({'file_url': file_url}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class QrCodeFileDownloadView(APIView):
    def get(self, request, file_name):
        file_path = os.path.join(settings.QRCODE_MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
            file = open(file_path, 'rb')
            response = FileResponse(file)
            return response
        else:
            return Response({'error': 'File not found.'}, status=status.HTTP_404_NOT_FOUND)


class SecureRepoFileDownloadView(APIView):
    def get(self, request, file_name):
        file_path = os.path.join(settings.SECURE_REP0_MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
            file = open(file_path, 'rb')
            response = FileResponse(file)
            return response
        else:
            return Response({'error': 'File not found.'}, status=status.HTTP_404_NOT_FOUND)
        
class AnnouncementFileDownloadView(APIView):
    def get(self, request, file_name):
        file_path = os.path.join(settings.ANNOUNCEMENT_MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
            file = open(file_path, 'rb')
            response = FileResponse(file)
            return response
        else:
            return Response({'error': 'File not found.'}, status=status.HTTP_404_NOT_FOUND)