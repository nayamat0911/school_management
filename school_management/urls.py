from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views,hod_views,student_views,staff_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('app/', include('school.urls')),
   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

