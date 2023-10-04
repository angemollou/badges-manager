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


user.BadgeUser.assert_badge = assert_badge
