from django.contrib import admin
from core.models import UserLoginRecord


@admin.register(UserLoginRecord)
class ExpressOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'userID', 'username', 'detail']
    # search_fields = ['project_code', 'company', 'order_number', 'to_people', 'sendDate']
    # ordering = ("project_code",)
    # list_per_page = 100
    # list_editable = ['content']
    # list_display_links = ('company', 'order_number',)
    # list_filter = ('project_code', 'sendDate')
    # date_hierarchy = 'sendDate'
