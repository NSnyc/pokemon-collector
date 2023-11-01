from django.shortcuts import render

from django.http import HttpResponse

from main_app.models import Pokemon

# Add the Pokemon class & list and view function below the imports
# class Pokemon:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# pokemon = [
#   Pokemon('Lolo', 'tabby', 'Kinda rude.', 3),
#   Pokemon('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#   Pokemon('Fancy', 'bombay', 'Happy fluff ball.', 4),
#   Pokemon('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

# Define the home view
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