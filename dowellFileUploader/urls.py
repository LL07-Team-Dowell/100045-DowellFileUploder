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
    path('media/QrCodes/<path:path>', serve, {'document_root': settings.QRCODE_MEDIA_ROOT}),
    path('media/SecureRepo/<path:path>', serve, {'document_root': settings.SECURE_REP0_MEDIA_ROOT}),
]