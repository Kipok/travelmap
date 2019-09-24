from django.contrib import admin

from . import models


class TravelImageInline(admin.TabularInline):
    model = models.TravelImage
    extra = 1


@admin.register(models.TravelRecord)
class TravelRecordAdmin(admin.ModelAdmin):
    inlines = [TravelImageInline]
