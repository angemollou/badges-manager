from django.contrib import admin
from .models.badge import Badge, Assertion
from .models.model3d import Model3d
from .models.user import BadgeUser

admin.site.register(Badge)
admin.site.register(Model3d)
admin.site.register(BadgeUser)
admin.site.register(Assertion)