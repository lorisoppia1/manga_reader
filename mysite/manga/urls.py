from django.urls import path
from .views import MangaAPI, TestAPI

urlpatterns = [
    path('manga/', MangaAPI.as_view()),
    path('test/', TestAPI.as_view())
]