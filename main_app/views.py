from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Puppy, Toy
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

# Add new view
@login_required
def puppy_index(request):
  puppies = Puppy.objects.filter(user=request.user)
  return render(request, 'puppies/index.html', { 'puppies': puppies })

@login_required
def puppy_detail(request, puppy_id):
  puppy= Puppy.objects.get(id=puppy_id)
  toys_puppy_doesnt_have = Toy.objects.exclude(id__in = puppy.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'puppies/detail.html', { 
    'puppy': puppy,
    'feeding_form': feeding_form,
    'toys': toys_puppy_doesnt_have
  })

@login_required
def add_feeding(request, puppy_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.puppy_id = puppy_id
    new_feeding.save()
  return redirect('puppy-detail', puppy_id=puppy_id)

@login_required
def assoc_toy(request, puppy_id, toy_id):
  Puppy.objects.get(id=puppy_id).toys.add(toy_id)
  return redirect('puppy-detail', puppy_id=puppy_id)

class PuppyCreate(LoginRequiredMixin, CreateView):
  model= Puppy
  fields = ['name', 'breed', 'description', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PuppyUpdate(LoginRequiredMixin, UpdateView):
  model= Puppy
  fields = ['breed', 'description', 'age']

class PuppyDelete(LoginRequiredMixin, DeleteView):
  model= Puppy
  success_url = '/puppies/'

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)