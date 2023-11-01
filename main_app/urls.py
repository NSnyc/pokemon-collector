from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pokemon/', views.pokemon_index, name='pokemon-index'),
  path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='pokemon-detail'),
  path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon-create'),
  path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon-update'),
  path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon-delete'),
  path('pokemon/<int:pokemon_id>/add_feeding/', views.add_feeding, name='add-feeding'),
  path('items/create/', views.Held_ItemCreate.as_view(), name='held-item-create'),
]