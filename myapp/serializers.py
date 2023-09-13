from rest_framework import serializers
from .models import PriohubItem

class PriohubItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriohubItem
        fields = '__all__'
