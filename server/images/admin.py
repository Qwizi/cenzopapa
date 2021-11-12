from django.contrib import admin

from images.models import Image


@admin.action(description='Validate images')
def make_validated(modelAdmin, request, queryset):
    queryset.update(is_validated=True)

@admin.action(description='Unvalidate images')
def make_unvalidated(modelAdmin, request, queryset):
    queryset.update(is_validated=False)


class ImageAdmin(admin.ModelAdmin):
    list_filter = [
        "is_validated",
    ]
    list_display = (
        'id',
        'posted_at',
        'height',
        'width',
        'is_validated'
    )

    actions = [make_validated, make_unvalidated]


admin.site.register(Image, ImageAdmin)
