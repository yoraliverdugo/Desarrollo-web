from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewSet, basename = 'products' )
router.register('categories', CategoryViewSet, basename = 'categories')


urlpatterns = [
    path('', include(router.urls))
]
