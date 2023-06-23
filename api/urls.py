from django.urls import path, include
from knox.views import LogoutView
from rest_framework.routers import DefaultRouter

from api.views import HealthyView, CheckAnswerView, RegistrationAPIView, LoginView, ProfileAPIView
from api.wagtail_urls import router as wagtail_router


router = DefaultRouter()

urlpatterns = [
    path('healthy/', HealthyView.as_view()),
    path('check_answer/', CheckAnswerView.as_view()),
    path('wagtail/', wagtail_router.urls),
    path('profile/', ProfileAPIView.as_view()),
    path('auth/login/', LoginView.as_view(), name='knox_login'),
    path('auth/logout/', LogoutView.as_view(), name='knox_logout'),
    path('auth/registration/', RegistrationAPIView.as_view()),
]
urlpatterns += router.urls
