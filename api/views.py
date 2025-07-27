from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import OAuth2Authentication

class ProtectedResource(APIView):
    authentication_classes = [OAuth2Authentication]  # Используем OAuth2 для аутентификации
    permission_classes = [IsAuthenticated]  # Доступ только авторизованным пользователям

    def get(self, request):
        return Response({"message": "Вы успешно авторизовались!", "user": request.user.username})
