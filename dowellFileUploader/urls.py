from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploadfiles/', include('fileUploader.urls')),
]

urlpatterns += [
    path('qrCodes/<path:path>',                 serve, {'document_root': settings.QRCODE_MEDIA_ROOT}),
    path('secureRepo/<path:path>',              serve, {'document_root': settings.SECURE_REP0_MEDIA_ROOT}),
    path('announcements/<path:path>',           serve, {'document_root': settings.ANNOUNCEMENT_MEDIA_ROOT}),
    path('camera_component_images/<path:path>', serve, {'document_root': settings.CAM_COMPONENT_IMAGES_MEDIA_ROOT}),
    path('camera_component_videos/<path:path>', serve, {'document_root': settings.CAM_COMPONENT_VIDEOS_MEDIA_ROOT}),
    path('publicSecureRepo/<path:path>',        serve, {'document_root': settings.PUBLIC_SECURE_REP0_MEDIA_ROOT}),
    path('digitalQueue/<path:path>',            serve, {'document_root': settings.DIGITAL_QUEUE_MEDIA_ROOT}),
    path('publicSecureRepo/<path:path>', serve, {'document_root': settings.PUBLIC_SECURE_REP0_MEDIA_ROOT}),

    path('view-pdf/<path:path>', serve, {'document_root': settings.SAVE_PDF}),
    path('hr/<path:path>', serve, {'document_root': settings.HR_MEDIA_ROOT}),
    path('voice-recording/<path:path>', serve, {'document_root': settings.VOICE_RECORDING})
]