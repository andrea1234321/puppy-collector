from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('puppies/', views.puppy_index, name='puppy-index'),
  path('puppies/<int:puppy_id>', views.puppy_detail, name='puppy-detail'),
  path('puppies/create/', views.PuppyCreate.as_view(), name='puppy-create'),
  path('puppies/<int:pk>/update/', views.PuppyUpdate.as_view(), name='puppy-update'),
  path('puppies/<int:pk>/delete/', views.PuppyDelete.as_view(), name='puppy-delete'),
  path('puppies/<int:puppy_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
  path('puppies/<int:puppy_id>/assoc-toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
]