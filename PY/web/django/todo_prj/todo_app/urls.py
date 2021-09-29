from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(f'ToDo', views.ToDoViewSet)

# Wire up our API using automatic URL routing.
# A router works with a viewset to dynamically route requests.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
