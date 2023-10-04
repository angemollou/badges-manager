from django.conf import settings
from django.urls import include, path
from .views import index
from rest_framework import routers
from badge import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"badgeUsers", views.BadgeUserViewSet)
router.register(r"model3ds", views.Model3dViewSet)
router.register(r"badges", views.BadgeViewSet)
router.register(r"assertions", views.AssertionViewSet)

urlpatterns = [
    path("", index.index, name="index"),
    path("", include(router.urls)),
]

if settings.DEBUG == True:
    # Include default login and logout views for use with the browsable API
    urlpatterns.append(
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))
    )
