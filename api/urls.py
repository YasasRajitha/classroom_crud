from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenBlacklistView

from . import views

router = DefaultRouter()
router.register('addtask',views.TaskViewSet,basename='addtask')
router.register('addtaskstatus',views.TaskStatusViewSet,basename='addtaskstatus')

urlpatterns = [
    path('',include(router.urls)),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('token/blacklist/',TokenBlacklistView.as_view(),name='token_blacklist'),
]