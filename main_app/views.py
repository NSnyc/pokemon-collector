from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from main_app.models import Pokemon
from .models import Pokemon, Held_Item
from .forms import FeedingForm

class Held_ItemList(LoginRequiredMixin, ListView):
  model = Held_Item

class Held_ItemDetail(LoginRequiredMixin, DetailView):
  model = Held_Item

class Held_ItemCreate(LoginRequiredMixin, CreateView):
  model = Held_Item
  fields = '__all__'

class Held_ItemUpdate(LoginRequiredMixin, UpdateView):
  model = Held_Item
  fields = ['name', 'color']

class Held_ItemDelete(LoginRequiredMixin, DeleteView):
  model = Held_Item
  success_url = '/items/'

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def pokemon_index(request):
  pokemon=Pokemon.objects.filter(user=request.user)
  return render(request, 'pokemon/index.html', {'pokemon': pokemon})

@login_required
def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  held_items_pokemon_doesnt_have = Held_Item.objects.exclude(id__in = pokemon.held_items.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'pokemon/detail.html', {
    'pokemon': pokemon, 'feeding_form': feeding_form, 'held_items': held_items_pokemon_doesnt_have
  })

class PokemonCreate(LoginRequiredMixin, CreateView):
  model = Pokemon
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/pokemon/'
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PokemonUpdate(LoginRequiredMixin, UpdateView):
  model = Pokemon
  fields = ['breed', 'description', 'age']

class PokemonDelete(LoginRequiredMixin, DeleteView):
  model = Pokemon
  success_url = '/pokemon/'

def add_feeding(request, pokemon_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.pokemon_id = pokemon_id
    new_feeding.save()
  return redirect('pokemon-detail', pokemon_id=pokemon_id)

@login_required
def assoc_item(request, pokemon_id, held_item_id):
  Pokemon.objects.get(id=pokemon_id).held_items.add(held_item_id)
  return redirect('pokemon-detail', pokemon_id=pokemon_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('pokemon-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)