from django.urls import path
from . import views
from .views import groupeprojet_list, groupeprojet_detail, groupeprojet_create, groupeprojet_update, groupeprojet_delete

urlpatterns = [
    path('groupes/', groupeprojet_list, name='groupeprojet_list'),
    path('groupes/<int:pk>/', groupeprojet_detail, name='groupeprojet_detail'),
    path('groupes/add/', groupeprojet_create, name='groupeprojet_create'),
    path('groupes/<int:pk>/edit/', groupeprojet_update, name='groupeprojet_update'),
    path('groupes/<int:pk>/delete/', groupeprojet_delete, name='groupeprojet_delete'),
]
