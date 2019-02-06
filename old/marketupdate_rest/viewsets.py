from rest_framework import viewsets, filters
from marketupdate_rest.serializers import * # import our serializer
from marketupdate_model.models import Update, Category, Symbol, Value, all_last_update_v


class UpdateViewSet(viewsets.ModelViewSet):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer

class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer

class AllLastUpdateSet(viewsets.ModelViewSet):
    queryset = all_last_update_v.objects.all()
    serializer_class = AllLastUpdateSerializer