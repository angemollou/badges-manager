import logging
from django_cron import CronJobBase, Schedule

logger = logging.getLogger("badge")


class AssertBadgeJob(CronJobBase):
    RUN_EVERY_MINS = 24  # every 24 secs

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "badge.assert_badge_job"  # a unique code

    def do(self):
        logger.info("AssertBadge cron job started -------------------------------------->")
        # TODO : detect if user deserves a badges based on his score
        pass
        logger.info("AssertBadge cron job ended --------------------------------------<")
