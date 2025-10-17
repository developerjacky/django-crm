from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('<int:people_id>', views.detail, name="detail"),
    path('add/', views.add_people, name='add_people'),
    path('edit/<int:people_id>/', views.edit_people, name='edit_people'),
    path('delete/<int:people_id>/', views.delete_people, name='delete_people'),    
]


