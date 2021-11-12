from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('memberslogin/', include('django.contrib.auth.urls')),
    path('memberslogin/', include('memberslogin.urls')),
]
