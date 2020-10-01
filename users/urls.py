from django.urls import path
from .views import login_view, sign_up_view, update_profile_view

urlpatterns = [
  path('login/', login_view, name="login"),
  path('sign-up/', sign_up_view, name="signup"),
  path('me/profile/', update_profile_view, name="update_profile"),
]