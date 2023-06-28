from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploadfiles/', include('fileUploader.urls')),
    path('api/v2/', include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('media/qrCodes/<path:path>', serve, {'document_root': settings.QRCODE_MEDIA_ROOT}),
    path('media/secureRepo/<path:path>', serve, {'document_root': settings.SECURE_REP0_MEDIA_ROOT}),
    path('media/announcements/<path:path>', serve, {'document_root': settings.ANNOUNCEMENT_MEDIA_ROOT}),
    path('media/Image/<path:path>', serve, {'document_root': settings.CAM_COMPONENT_IMAGES_MEDIA_ROOT}),
    path('media/Video/<path:path>', serve, {'document_root': settings.CAM_COMPONENT_VIDEOS_MEDIA_ROOT}),

    
]