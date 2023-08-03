from rest_framework import serializers
from . models import Store




class CreateStoreSerializer(serializers.ModelField):
    class Meta:
        model = Store
        fields = "__all__"