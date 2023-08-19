from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^setting/', include('setting.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^operation/', include('operation.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)