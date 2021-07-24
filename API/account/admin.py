from account.models import Account
from django.contrib import admin

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'username', 'first_name', 'last_name', )

    class Meta:
        ordering = ("id")
admin.site.register(Account, AccountAdmin)