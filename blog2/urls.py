from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/',views.about , name = 'blog-about'),
    path('about/contact/',views.contact , name = 'blog-contact'),
    path('about/contact/stores', views.stores, name = 'blog-stores'),
]
