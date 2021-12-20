from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("profile", views.profile, name="profile"),
    path("accounts/profile/", views.profile, name="profile"),
    
]