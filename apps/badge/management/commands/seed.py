from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from badge.models.badge import Badge
from badge.models.model3d import Model3d
from django.contrib.auth.models import User
from badge.models.user import BadgeUser
from badge.models.task import Task

from ...data.badge import BADGE_DATA, MODEL3D_DATA
from ...data.demo.task import TASK_DATA

""" Clear all data and creates badges """
MODE_REFRESH = "refresh"
""" Clear all data and do not create any object """
MODE_CLEAR = "clear"


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        self.run_seed(options["mode"])
        self.stdout.write("done.")

    def run_seed(self, mode):
        """Seed database based on mode

        :param mode: refresh / clear
        :return:
        """
        # Clear data from tables
        self.clear_data()
        if mode == MODE_CLEAR:
            return

        # Insert badges data
        for model3d_data, badge_data in zip(MODEL3D_DATA, BADGE_DATA):
            self.create_badge(model3d_data, badge_data)

        # Create BadgeUsers
        self.create_badge_users()

        # Insert demo data
        if settings.DEBUG:
            self.stdout.write("Creating demo data")
            self.create_demo_task()

    def clear_data(self):
        """Deletes all the table data"""
        self.stdout.write("Delete Badge instances")
        try:
            Badge.objects.all().delete()
        except Exception as e:
            raise CommandError(e)

    def create_badge(self, model3d_data, badge_data):
        """Creates an badge object combining different elements from the list"""
        try:
            self.stdout.write("Creating badge")
            model3d = Model3d(**model3d_data)
            model3d.save()
            badge = Badge(**badge_data, icon=model3d)
            badge.save()
            self.stdout.write("{} badge created.".format(badge))
            return badge
        except Exception as e:
            raise CommandError(e)

    def create_badge_users(self):
        """Creates badge users from admins accounts"""
        try:
            self.stdout.write("Creating badge users")
            badge_users = []
            for user in User.objects.all():
                badge_user = BadgeUser(user=user)
                badge_user.save()
                self.stdout.write("Asserting {} the default badge".format(badge_user))
                badge_user.assert_badge()
                self.stdout.write("{} badge user created.".format(badge_user))
                badge_users.append(badge_user)
            return badge_users
        except Exception as e:
            raise CommandError(e)

    def create_demo_task(self):
        """Creates demo task"""
        try:
            self.stdout.write("Creating demo task")
            for item in TASK_DATA:
                task = Task(**item)
                task.save()
                self.stdout.write("{} task created.".format(task))
        except Exception as e:
            raise CommandError(e)
