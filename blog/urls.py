from django.urls import path, include
from blog.views import RegisterView, LoginView, UserViewSet, PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'profile', UserViewSet, basename='profile')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

