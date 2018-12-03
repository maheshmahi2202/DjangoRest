from rest_framework import serializers
from .models import TestResults

class Testresultserializer(serializers.ModelSerializer):

    class Meta:
        model = TestResults
        fields = '__all__'


