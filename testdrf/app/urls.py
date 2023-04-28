from django.urls import path
from .views import EntityAPIVew, CreateEntityAPI


urlpatterns =[
    path('entity/', EntityAPIVew.as_view()),
    path('entity_add/', CreateEntityAPI.as_view())
]