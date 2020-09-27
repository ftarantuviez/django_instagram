from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from platzigram import views as local_views


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('hello/', local_views.hello_world, name="hello_world"),
    path('hi/', local_views.hi, name="hi"),
    path('sorted/<str:name>/<int:age>/', local_views.params, name="sorted"),

    path('', include('posts.urls')),
    path('users/', include('users.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)