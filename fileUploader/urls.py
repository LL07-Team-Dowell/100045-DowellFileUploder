
from django.urls import path
from .views import *
urlpatterns = [
    path('upload-files-to-drive/', FileCreateView.as_view(), name='file-create'),
]
