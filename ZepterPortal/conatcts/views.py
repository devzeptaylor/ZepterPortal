from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from conatcts.models import Telefon
from conatcts.serializers import TelefonSerializer

from django.shortcuts import render
from .models import OracleData

# Create your views here.
def contacts_page(request ):
    return render(request, 'oldindex.html',{'telefons': Telefon.objects.all()})

#class TelefonView (ModelViewSet):
#    queryset = Telefon.objects.all()
#    serializer_class = TelefonSerializer

class TelefonView (ModelViewSet):
    queryset = Telefon.objects.all()
    serializer_class = TelefonSerializer

def order_app(request ):
    return render(request, 'index.html')

def show_stat(request):
    return render(request,'tables.html',{'telefons': Telefon.objects.all()})

def show_oracle_data(request):
    oracle_data = OracleData.objects.using('oracle_db').all()  # запрос к Oracle
    return render(request, 'your_template.html', {'oracle_data': oracle_data})