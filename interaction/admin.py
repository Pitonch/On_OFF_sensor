from django.contrib import admin
from .models import Home, Location, Sensor


# admin.site.register(Home)
# admin.site.register(Location)
# admin.site.register(Sensor)

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name_home', 'descriptions_home',)
    ordering = ('name_home',)
    search_fields = ('name_home',)


@admin.register(Location)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name_location', 'descriptions_location', 'home',)
    ordering = ('name_location',)
    search_fields = ('name_location',)


@admin.register(Sensor)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('ip_sensor', 'status', 'name_sensor', 'descriptions_sensor', 'location', 'home_name',)
    ordering = ('name_sensor',)
    search_fields = ('name_sensor',)
    list_filter = ('name_sensor', 'location',)

    @admin.display()
    def home_name(self, obj: Sensor):
        return Home.objects.get(name_home=obj.name_sensor).name_home
