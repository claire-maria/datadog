from django.urls import path
from . import views

urlpatterns = [

    path('pets/add_pet', views.edit_pets, name = 'add_pet'),
    path('pets/edit/<int:pet_id>', views.edit_pets, name = 'edit_pet'),
     path('pets/delete/<int:pet_id>', views.del_pet, name = 'del_pet'),
    path('', views.index, name = 'index'),
]