from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Puppy:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

puppies = [
  Puppy('Emi', 'Aussie mix', "Doesn't like when you stare at her", 2),
  Puppy('April', 'mix', 'Eats more than she should', 8),
  Puppy('Lola', 'malteese', 'Happy fluff ball.', 5),
  Puppy('Jasper', 'malteese', 'Angel', 12)
]
# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def puppy_index(request):
  return render(request, 'puppies/index.html', { 'puppies': puppies })
