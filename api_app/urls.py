from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


# creating router Object
router = DefaultRouter()
# Registering the ViewSet with router

router.register('singer', views.SingerViewSet,basename='singer')
router.register('song',views.SongViewSet, basename='song')


urlpatterns = [
    # This is for the authentication auth login purpose.
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]