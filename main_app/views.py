from django.shortcuts import render

from django.http import HttpResponse

# Add the Pokemon class & list and view function below the imports
class Pokemon:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, temperment, description, age):
    self.name = name
    self.temperment = temperment
    self.description = description
    self.age = age

pokemon = [
  Pokemon('Lolo', 'tabby', 'Kinda rude.', 3),
  Pokemon('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Pokemon('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Pokemon('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Future Champions! ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  return render(request, 'pokemon/index.html', {'pokemon': pokemon})