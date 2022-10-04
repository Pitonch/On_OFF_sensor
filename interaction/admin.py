from django.contrib import admin
from .models import Home, Location, Sensor


# admin.site.register(Home)
# admin.site.register(Location)
# admin.site.register(Sensor)

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions',)
    ordering = ('name',)
    search_fields = ('name',)

    #
    # @admin.display(description='Описание')
    # def home_name(self, obj: Home):










@admin.register(Location)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions', 'home',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Sensor)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('ip', 'name', 'descriptions', 'location',)
    ordering = ('name',)
    search_fields = ('name',)
