from django.urls import path
from .views import *
urlpatterns = [
    path('upload-qrcode-to-drive/',      QrCodeUploadView.as_view(),         name='qrcode_upload'),
    path('upload-secure-repo-to-drive/', SecureRepoFileUploadView.as_view(), name='secure_repo_upload'),

    path('qrcode-download/<str:file_name>/', QrCodeFileDownloadView.as_view(),     name='qrcode-download'),
    path('secure-repo-download-file/<str:file_name>/', SecureRepoFileDownloadView.as_view(), name='secure-repo-download'),
]
