from django.contrib.auth.models import User
from badge.models.user import BadgeUser
from badge.models.model3d import Model3d
from badge.models.badge import Badge, Assertion
from rest_framework import viewsets
from rest_framework import permissions
from badge.serializers import (
    UserSerializer,
    BadgeUserSerializer,
    Model3dSerializer,
    BadgeSerializer,
    AssertionSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class BadgeUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows badge users to be viewed or edited.
    """

    queryset = BadgeUser.objects.all().order_by("-id")
    serializer_class = BadgeUserSerializer
    permission_classes = [permissions.IsAuthenticated]



class Model3dViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows model3ds to be viewed or edited.
    """

    queryset = Model3d.objects.all().order_by("-id")
    serializer_class = Model3dSerializer
    permission_classes = [permissions.IsAuthenticated]



class BadgeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows badges to be viewed or edited.
    """

    queryset = Badge.objects.all().order_by("-id")
    serializer_class = BadgeSerializer
    permission_classes = [permissions.IsAuthenticated]



class AssertionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assertions to be viewed or edited.
    """

    queryset = Assertion.objects.all().order_by("-id")
    serializer_class = AssertionSerializer
    permission_classes = [permissions.IsAuthenticated]