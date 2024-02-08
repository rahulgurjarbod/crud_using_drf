from . import views
from django.urls import path


urlpatterns = [
    path('get_person/<str:pk>/', views.getPerson),
    path('get_person/', views.getAllPersons),
    path('create_person/', views.createPerson),
    path('update_person/<str:pk>/', views.updatePerson),
    path('partial_update/<str:pk>/', views.partialUpdate),
    path('delete_person/<str:pk>/',views.deletePerson),
]