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
    path("profile/update/", views.update_profile, name="update_profile"),
    path("post/save/", views.create_post, name="save_post"), # save post
    path("business/create/", views.create_business, name="create_business"), # create business
    path("contact/create/", views.create_contact, name="create_contact"), # create contact
    path("posts/", views.posts, name="posts"), # all posts
    path("alerts/", views.alerts, name="alerts"), # alerts
    path("business/", views.business, name="business"), # business
    path("contacts/", views.contacts, name="contacts"), # contacts
    path("search/", views.search, name="search"), # search
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)