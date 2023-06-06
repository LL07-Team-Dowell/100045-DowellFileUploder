from django.urls import path
from .views import *
urlpatterns = [
    path('upload-files-to-drive/',         FileCreateView.as_view(),   name='file-create'),
    path('download-file/<str:file_name>/', FileDownloadView.as_view(), name='file-download'),
]
