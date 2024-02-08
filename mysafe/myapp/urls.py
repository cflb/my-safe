# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmbienteViewSet, AplicacaoViewSet, SegredoViewSet

router = DefaultRouter()
router.register(r'ambientes', AmbienteViewSet)
router.register(r'aplicacoes', AplicacaoViewSet)
router.register(r'segredos', SegredoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
