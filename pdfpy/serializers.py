#Serializing The main Model
from .models import Collector , Display
from rest_framework import serializers


class CollectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collector
        fields = ['pdf_file']

class DisplaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Display
        fields = ['mostcommon']