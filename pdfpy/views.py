from django.shortcuts import render
from .models import Collector
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CollectorSerializer 


class CollectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Collector.objects.all()
    serializer_class = CollectorSerializer
    permission_classes = [permissions.IsAuthenticated]



