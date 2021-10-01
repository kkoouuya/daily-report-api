from rest_framework import routers
from django.urls import path, include
from .views import DailyViewSet, CategoryAPI

router = routers.DefaultRouter()
router.register('dailys', DailyViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('category/<str:category>/', CategoryAPI.as_view())
]
