

from django.db.models.signals import post_init
from django.shortcuts import render, redirect
from pages.models import Currencies, CurrencySign
#from django.http import HttpResponse
from pages.forms import   CurrencyForm, CurrecnySignForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CurrenciesSerializer
from django.views import View


# Create your views here.
def index(request):
    #return HttpResponse('Index Page')
    x = {'Lang':'English',
         'age':27
         }
    return render(request,'pages/index.html',x)

def main(request):
     return render(request,'pages/main.html')


def about(request):
     return render(request,'pages/about.html')


def html_js(request):
     return render(request,'pages/html_js.html')

def home(request):
     return render(request,'pages/home.html')

def image_slide(request):
    return render(request, 'pages/image_slide.html')

def navbar(request):
    return render(request,'pages/navbar.html')

def navbar_template(request):
    return render(request,'pages/navbar_template.html')


def create_currency_sign(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            cur_sign = form.cleaned_data['cur_sign']
            sign = form.cleaned_data['sign']
            currencies_sign =  CurrecnySignForm.objects.create(cur_sign=cur_sign,sign=sign)            
            return redirect('/index')
    else:
        form = CurrecnySignForm()
        return render(request, 'pages/create_currency_sign.html',{
            'form': form
    })


def create_currency(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            cur_id = form.cleaned_data['cur_id']
            cur_name = form.cleaned_data['cur_name']
            cur_sign = form.cleaned_data['cur_sign']
            cur_tag = form.cleaned_data['cur_tag']
            currencies =  Currencies.objects.create(cur_id=cur_id,cur_name=cur_name,cur_sign=cur_sign)
            currencies.cur_tag.set(cur_tag)
            return redirect('/ist_currencies')
    else:
        form = CurrencyForm()
        return render(request, 'pages/create_currency.html',{
            'form': form
    })

def list_currencies(request):
    #models = Currencies.objects.order_by('cur_name')
    #models = Currencies.objects.all()[10:20]
    #models = Currencies.objects.filter(cur_id__gte=3)
    #models = Currencies.objects.filter(cur_id__range=(1,3))
    #models = Currencies.objects.filter(cur_name__contains='دي')
    #models = Currencies.objects.filter(cur_name__icontains='دي')
    #models = Currencies.objects.filter(cur_name__startswith='ريال')
    #models = Currencies.objects.filter(cur_name__endswith='دي')
    #models = Currencies.objects.select_related('field').all()
    # models = Currencies.objects.prefetch_related('field').all()

    models = Currencies.objects.select_related('cur_sign').prefetch_related('cur_tag').all()
    #select_related(CurrencySign)

    return render(request, 'pages/list_currencies.html',
                  {
                      'currencies': models
                  })

def show_currency(request, id):
    #models = Currencies.objects.get(pk=id)
    models = Currencies.objects.filter(pk=id).first()
    return render(request, 'pages/show_currency.html',
                  {
                      'currencies': models
                  })

def update_currency(request, id):
    Currencies.objects.filter(pk=id).update(cur_sign ='y&')
    currncies = Currencies.objects.get(pk=id)
    return render(request, 'pages/update_currency.html',
                  {
                      'currencies': currncies
                  })

def delete_currency(request, id):
    Currencies.objects.filter(pk=id).delete()
    currncies = Currencies.objects.all()
    return redirect ('/list_currencies')



#API configuration
class CurrenciesList(APIView):
    def get(self, request):
        currencies = Currencies.objects.prefetch_related('cur_tag').all()
        serializer = CurrenciesSerializer(currencies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CurrenciesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
