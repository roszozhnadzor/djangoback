from .models import *
from rest_framework import serializers


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Cakes
        # Поля, которые мы сериализуем
        fields = ["id", "name", "pricekg", "taste"]

class TasteSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Tastes
        # Поля, которые мы сериализуем
        fields = ["id", "nameid", "discription"]