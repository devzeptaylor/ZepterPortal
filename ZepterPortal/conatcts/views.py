from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from conatcts.models import Telefon
from conatcts.serializers import TelefonSerializer


# Create your views here.
def contacts_page(request ):
    return render(request, 'index.html',{'telefons': Telefon.objects.all()})

class TelefonView (ModelViewSet):
    queryset = Telefon.objects.all()
    serializer_class = TelefonSerializer

def order_app(request ):
    return render(request, 'main_app.html')
