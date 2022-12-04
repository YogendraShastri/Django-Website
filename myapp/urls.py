from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blogPost/<int:id>',views.blogPost, name='post'),
    path('search',views.search,name='search'),
    path('signup',views.signup,name='signup'),
]