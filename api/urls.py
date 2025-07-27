from django.urls import path
from .views import ProtectedResource

urlpatterns = [
    path('protected/', ProtectedResource.as_view(), name='protected'),  # Обработчик защищённого API
]
