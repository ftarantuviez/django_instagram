from django.urls import path
from .views import *

urlpatterns = [
    path('feed/', list_posts, name="feed")
]