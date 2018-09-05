from django.shortcuts import render
from .serializers import BusSerializer
from .models import *
from rest_framework import viewsets

class BusViewset(viewsets.ModelViewSet):
    serializer_class=BusSerializer
    queryset= Bus.objects.all()

def stringdisplay(request):

    str=String.objects.all().values()

    return render(request,'string.html',{'str':str})