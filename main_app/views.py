from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Pokemon
from main_app.models import Pokemon


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  pokemon=Pokemon.objects.all()
  return render(request, 'pokemon/index.html', {'pokemon': pokemon})

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  return render(request, 'pokemon/detail.html', {'pokemon': pokemon})

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'
  success_url = '/pokemon/'