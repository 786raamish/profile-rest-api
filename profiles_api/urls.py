from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

# 2 With ViewSet, note1: Not mention base_name
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, 'hello-viewset')


# 1 With API Views
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    # 2.1
    path('', include(router.urls))
]
