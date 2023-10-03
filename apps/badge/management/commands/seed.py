from django.core.management.base import BaseCommand, CommandError
from badge.models.badge import Badge
from badge.models.model3d import Model3d
from ...data.badge import BADGE_DATA, MODEL3D_DATA

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

        # Creating 15 badges
        for model3d_data, badge_data  in zip(MODEL3D_DATA, BADGE_DATA):
            self.create_badge(model3d_data, badge_data)

    def clear_data(self):
        """Deletes all the table data"""
        self.stdout.write("Delete Badge instances")
        Badge.objects.all().delete()

    def create_badge(self, model3d_data, badge_data):
        """Creates an badge object combining different elements from the list"""
        self.stdout.write("Creating badge")
        model3d = Model3d(**model3d_data)
        model3d.save()
        badge = Badge(**badge_data, icon=model3d)
        badge.save()
        self.stdout.write("{} badge created.".format(badge))
        return badge
