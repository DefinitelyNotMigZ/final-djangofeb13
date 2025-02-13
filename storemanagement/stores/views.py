from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users,Stores
from .serializers import StoreSerializer, UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    permission_classes=[]
    queryset = Users.objects.all()
    serializer_class=UserSerializer

class StoresViewSet(viewsets.ModelViewSet):
    permission_classes=[]
    queryset = Stores.objects.all()
    serializer_class=StoreSerializer
