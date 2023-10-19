import logging

from . import user
from . import model3d
from . import badge
from . import task
from django.db.models import Q


logger = logging.getLogger(__name__)


def assert_badge(self, new_badge=False, verifier=False):
    """Assert user the default badge"""
    try:
        new_badge = new_badge or badge.Badge.objects.get(
            Q(name="Default") | Q(criteria=0)
        )
        assertion = badge.Assertion(
            recipient=self,
            badge=new_badge,
            verifier=verifier or self,
        )
        assertion.save()
        logger.info("{} badge assertion created.".format(assertion))
        return assertion
    except Exception as e:
        raise e


def try_assert_badge(self):
    """Detect and assert to user who deserve it"""
    try:
        badges = badge.Badge.objects.filter(Q(criteria__lt=self.score))
        assertions = []
        for new_badge in badges:
            if new_badge not in map(lambda a: a.badge, self.assertions.all()):
                assertions.append(self.assert_badge(new_badge))
        return assertions
    except Exception as e:
        raise e


def set_new_score(self, points):
    self.score += points
    self.try_assert_badge()
    self.save()
    return self.score


user.BadgeUser.assert_badge = assert_badge
user.BadgeUser.try_assert_badge = try_assert_badge
user.BadgeUser.set_new_score = set_new_score
