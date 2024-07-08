# travel/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, RegionViewSet, VisitedRegionViewSet, regions_by_country, visits_by_country

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'visitedregion', VisitedRegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<str:country_code>/regions/', regions_by_country, name='regions-by-country'),
    path('<str:country_code>/visits/', visits_by_country, name='visits-by-country'),
]