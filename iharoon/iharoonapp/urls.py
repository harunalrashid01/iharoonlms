from django.contrib import admin    
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.home),
    path("subject/<int:id>/", views.subject),
    path("subject/<int:id>/chapter/<int:pk>/", views.chapter),
    path("subject/<int:id>/chapter/<int:pk>/c/<int:dk>", views.content),
    path("about/", views.about),
    path("quiz/<int:id>", views.quiz),
    path("/logout", views.quiz),

]
