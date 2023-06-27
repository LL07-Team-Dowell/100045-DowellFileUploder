from django.urls import path
from .views import *

urlpatterns = [
    path('upload-image/', ImageUploadView.as_view(), name='image-upload'),
    path('upload-video/', VideoUploadView.as_view(), name='video-upload'),
]
