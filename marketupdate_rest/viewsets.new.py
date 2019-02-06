from rest_framework import viewsets, filters
from marketupdate_rest.serializers import * # import our serializer
from marketupdate_model.models import Update, Category, Symbol, Value, all_last_update_v

#for ayth test
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAuthenticatedOrReadOnly, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class UpdateViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SymbolViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)     
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer

class ValueViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)     
    queryset = Value.objects.all()
    serializer_class = ValueSerializer

class AllLastUpdateSet(viewsets.ModelViewSet):
    permission_classes = (ReadOnly,)    
    queryset = all_last_update_v.objects.all()
    serializer_class = AllLastUpdateSerializer