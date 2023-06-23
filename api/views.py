from knox.models import AuthToken
from knox.serializers import UserSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from wagtail.api.v2.views import PagesAPIViewSet

from cms.models import TestPage
from users.models import User


class HealthyView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({'status': 'Everything is fine, thanks'})


class CheckAnswerView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        test_obj = TestPage.objects.get(id=request.data.get('test_id'))
        is_correct = test_obj.correct_answer.strip().casefold() == request.data.get('picked_value').strip().casefold()
        return Response({'is_correct': is_correct})


class WagtailPagesAPIView(PagesAPIViewSet):
    renderer_classes = [JSONRenderer]
    name = 'pages'


class RegistrationAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            _, token = AuthToken.objects.create(user=user)
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(
            {'error_text': 'Пользователь с таким логином уже существует'},
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]


class ProfileAPIView(APIView):
    def get(self, request):
        return Response(UserSerializer(instance=request.user).data)
