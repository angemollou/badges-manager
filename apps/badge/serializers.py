from django.contrib.auth.models import User
from badge.models.user import BadgeUser
from badge.models.model3d import Model3d
from badge.models.badge import Badge, Assertion
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


class BadgeUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BadgeUser
        fields = ["user", "score", "badges"]


class Model3dSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model3d
        fields = ["name", "description", "image", "file"]


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge
        fields = ["name", "icon", "description", "status", "criteria"]


class AssertionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assertion
        fields = [
            "recipient",
            "badge",
            "start_date",
            "end_date",
            "verifier",
            "verification_date",
        ]
