from django.shortcuts import render
from .models import Collector,Display
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CollectorSerializer , DisplaySerializer

#ViewSet for Main Serializer
class CollectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Collector.objects.all()
    serializer_class = CollectorSerializer
    permission_classes = [permissions.IsAuthenticated]

class DisplayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Display.objects.all()
    serializer_class = DisplaySerializer


