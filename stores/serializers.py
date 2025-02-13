from rest_framework import serializers
from .models import Users, Stores

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = "__all__"



