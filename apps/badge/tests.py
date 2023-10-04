from django.test import TestCase
from django.contrib.auth.models import User
from .models.user import BadgeUser


class BadgeUserModelTests(TestCase):
    def test_set_new_score_badgeuser(self):
        """
        set_new_score(points_amount) returns True for a given BadgeUser who completed an action
        """
        future_badgeuser = BadgeUser(user=User(username="Alex", password="Alex's password"))
        result = future_badgeuser.set_new_score(future_badgeuser.score + 1000)
        self.assertEqual(future_badgeuser.score, 1000)
