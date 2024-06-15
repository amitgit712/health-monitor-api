from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InterpretViewSet, HealthPlanViewSet

router = DefaultRouter()
router.register(r'qna', InterpretViewSet, basename='interpret')
router.register(r'health-plan', HealthPlanViewSet, basename='health-plan')

urlpatterns = [
    path('', include(router.urls)),
]
