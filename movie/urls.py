from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('movie/', include('movies.urls')),
    path('review/', include('reviews.urls')),
    path('screening/', include('screening.urls')),
    #path('aud/',include('auditorums.urls')),
    path('seat/', include('seats.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
