from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from main_app.models import Pokemon
from .models import Pokemon, Held_Item
from .forms import FeedingForm

class Held_ItemList(ListView):
  model = Held_Item

class Held_ItemDetail(DetailView):
  model = Held_Item

class Held_ItemCreate(CreateView):
  model = Held_Item
  fields = '__all__'

class Held_ItemUpdate(UpdateView):
  model = Held_Item
  fields = ['name', 'color']

class Held_ItemDelete(DeleteView):
  model = Held_Item
  success_url = '/items/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  pokemon=Pokemon.objects.all()
  return render(request, 'pokemon/index.html', {'pokemon': pokemon})

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  held_items_pokemon_doesnt_have = Held_Item.objects.exclude(id__in = pokemon.held_items.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'pokemon/detail.html', {
    'pokemon': pokemon, 'feeding_form': feeding_form, 'held_items': held_items_pokemon_doesnt_have
  })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/pokemon/'

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['breed', 'description', 'age']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon/'

def add_feeding(request, pokemon_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.pokemon_id = pokemon_id
    new_feeding.save()
  return redirect('pokemon-detail', pokemon_id=pokemon_id)

def assoc_item(request, pokemon_id, held_item_id):
  Pokemon.objects.get(id=pokemon_id).held_items.add(held_item_id)
  return redirect('pokemon-detail', pokemon_id=pokemon_id)