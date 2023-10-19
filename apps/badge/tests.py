from django.test import TestCase
from django.contrib.auth.models import User
from .models.user import BadgeUser


class BadgeUserModelTests(TestCase):
    def test_assert_badge_badgeuser(self):
        """
        assert_badge() asserts a given badge to a user
        """
        future_badgeuser = BadgeUser(
            user=User(username="Alex", password="Alex's password")
        )
        result = len(future_badgeuser.badges.all())
        self.assertEqual(result, 1)

    def test_set_new_score_badgeuser(self):
        """
        set_new_score(points_amount) returns True for a given BadgeUser who completed an action
        """
        future_badgeuser = BadgeUser(
            user=User(username="Alex", password="Alex's password")
        )
        result = future_badgeuser.set_new_score(future_badgeuser.score + 1000)
        self.assertEqual(future_badgeuser.score, 1000)
