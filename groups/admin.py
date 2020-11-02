from django.contrib import admin
from . import models
# Register your models here.

# for tabular inline to edit model on same page as parent
class GroupMemberInLine(admin.TabularInLine):
    model = models.GroupMember

admin.site.register(models.Group)