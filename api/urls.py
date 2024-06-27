from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Home, RegisterView

router = DefaultRouter()

urlpatterns = [
    path('', Home.as_view(), name='ApiHpme'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/', include(router.urls)),
]
