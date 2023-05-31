from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Puppy
from .forms import FeedingForm


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def puppy_index(request):
  puppies = Puppy.objects.all()
  return render(request, 'puppies/index.html', { 'puppies': puppies })

def puppy_detail(request, puppy_id):
  puppy= Puppy.objects.get(id=puppy_id)
  feeding_form = FeedingForm()
  return render(request, 'puppies/detail.html', { 
    'puppy': puppy,
    'feeding_form': feeding_form
  })


class PuppyCreate(CreateView):
  model= Puppy
  fields = '__all__'

class PuppyUpdate(UpdateView):
  model= Puppy
  fields = ['breed', 'description', 'age']

class PuppyDelete(DeleteView):
  model= Puppy
  success_url = '/puppies/'
