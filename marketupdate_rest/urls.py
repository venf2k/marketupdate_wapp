from django.conf.urls import url, include
from rest_framework import routers
from marketupdate_rest.viewsets import * # import our viewsets

app_name = 'marketupdate_rest' 

router = routers.DefaultRouter()
router.register('updates', UpdateViewSet, 'updates')
router.register('categories', CategoryViewSet, 'categories')
router.register('symbols', SymbolViewSet, 'symbols')
router.register('values', ValueViewSet, 'values')
router.register('last_market_update', AllLastUpdateSet, 'last_market_update')

urlpatterns = [
    url(r'^', include(router.urls)),
]   