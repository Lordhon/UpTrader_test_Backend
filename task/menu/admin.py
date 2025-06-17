from django.contrib import admin

from menu.models import Menu, MenuItem

admin.site.register(Menu)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent')
    search_fields = ('title',)
admin.site.register(MenuItem, MenuItemAdmin)
