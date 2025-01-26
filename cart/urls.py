from django.urls import path, include
from .views import CartViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]