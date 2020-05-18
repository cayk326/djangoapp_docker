from django.contrib import admin

# Register your models here.
from app.models import itemmodel


@admin.register(itemmodel.Item)
class ItemAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'
