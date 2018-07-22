from django.contrib import admin
from . import models
from django import template
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model=models.GroupMember

admin.site.register(models.Group)
