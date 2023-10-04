from django.conf import settings
from django.urls import include, path
from .views import views, api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", api.UserViewSet)
router.register(r"badgeUsers", api.BadgeUserViewSet)
router.register(r"model3ds", api.Model3dViewSet)
router.register(r"badges", api.BadgeViewSet)
router.register(r"assertions", api.AssertionViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/<int:task_id>", views.detail, name="task_detail"),
    path("", include(router.urls)),
]

if settings.DEBUG == True:
    # Include default login and logout views for use with the browsable API
    urlpatterns.append(
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))
    )
