from django.urls import path
from .views import SignupView, UserListViewSet, UserStatisticView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', UserListViewSet)
router.register(r'', UserStatisticView)

urlpatterns = [
    path('signup', SignupView.as_view()),
]

urlpatterns = router.urls