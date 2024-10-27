# myapp/serializers.py
from rest_framework import serializers
from pages.models import Currencies

class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'
