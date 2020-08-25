#Serializing The main Model
from .models import Collector
from rest_framework import serializers


class CollectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collector
        fields = ['pdf_file']

