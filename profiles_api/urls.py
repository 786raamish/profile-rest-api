from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

# 2 With ViewSet, note1: Not mention base_name
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, 'hello-viewset')
# 3 Register our models viewset
router.register('profile', views.UserProfileViewSet)
# 4 Register UserProfileFeed
router.register('feed', views.UserProfileFeedViewSet)


# 1 With API Views
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    # 2.1
    path('', include(router.urls))
]
