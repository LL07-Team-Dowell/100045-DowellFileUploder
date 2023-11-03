from django.urls import path
from .views import *


urlpatterns = [
    path('upload-qrcode-to-drive/',      QrCodeUploadView.as_view(),         name='qrcode_upload'),
    path('upload-secure-repo-to-drive/', SecureRepoFileUploadView.as_view(), name='secure_repo_upload'),
    path('upload-announcement-to-drive/', AnnouncementFileUploadView.as_view(), name='announcement_upload'),
    path('upload-digtalq-to-drive/', DigitalQFileUploadView.as_view(), name='digitalq_upload'),
    
    path('upload-pdf-file/', PDFFileUploadView.as_view(), name='upload_pdf'),

    path('upload-video-to-drive/', VideoFileUploadView.as_view(), name='video-file-upload'),
    path('upload-image-to-drive/', ImageFileUploadView.as_view(), name='image-file-upload'),

    path('upload-video-to-drive/', VideoFileUploadView.as_view(), name='video_file_upload'),
    path('upload-image-to-drive/', ImageFileUploadView.as_view(), name='image_file_upload'),
    path('upload-hr-image/', HrImageUploadView.as_view(), name='hr_image_upload'),
    path('samanta-campaign/', SamantaImageUploadView.as_view(), name='samanta_image_upload'),

    
    path('qrcode-download/<str:file_name>/', QrCodeFileDownloadView.as_view(),     name='qrcode-download'),
    path('secure-repo-download-file/<str:file_name>/', SecureRepoFileDownloadView.as_view(), name='secure-repo-download'),
    path('announcement-download-file/<str:file_name>/', AnnouncementFileDownloadView.as_view(), name='announcement-download'),
    path('upload-public-secure-repo-to-drive/', PublicSecureRepoFileUploadView.as_view(), name='secure_repo_upload'),
    path('secure-public-repo-download-file/<str:file_name>/', PublicSecureRepoFileDownloadView.as_view(), name='secure-repo-download'),
    path('digitalq-download-file/<str:file_name>/', DigitalQFileDownloadView.as_view(), name='digitalq-download'),
    path('hr-image-download/<str:file_name>/', HrImageDownloadView.as_view(),     name='hr-download'),

    path('upload-audio-to-drive/', VoiceRecordingFileUploadView.as_view(), name='audio-file-upload'),

]
