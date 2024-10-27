from django.urls import path
from . import views
from .views import  CurrenciesList

urlpatterns = [
    path('',views.index,name='index'),
    path('main', views.main, name='main'),
    path('about',views.about,name='about'),
    path('html_js', views.html_js, name='html_js'),
    path('home', views.home, name='home'),
    path('image_slide', views.image_slide, name='image_slide'),
    path('create_currency', views.create_currency, name='create_currency'),
    path('create_currency_sign', views.create_currency_sign, name='create_currency_sign'),
    path('list_currencies', views.list_currencies, name='list_currencies'),
    path('show_currency/<int:id>', views.show_currency, name='show_currency'),
    path('update_currency/<int:id>', views.update_currency, name='update_currency'),
    path('delete_currency/<int:id>', views.delete_currency, name='delete_currency'),
    path('navbar', views.navbar, name='navbar'),
    path('navbar_template', views.navbar_template, name='navbar_template'),
    path('currencies_list/', CurrenciesList.as_view(), name='currencies_list'),
    
]