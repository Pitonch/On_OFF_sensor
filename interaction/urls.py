from django.urls import path, re_path
from interaction import views as interaction_views


# POST
# /interaction/

urlpatterns = [
    path('about/', interaction_views.about, name='url_to_about'),
    path('settings/', interaction_views.settings, name='url_to_settings'),
    path('allsensors/', interaction_views.show_sensors, name='all_sensors'),
    path('commands/', interaction_views.commands, name='url_to_commands'),
    path('commands/<status>', interaction_views.sensor_on_off, name='sensor'),
    path('commands/<ip_>', interaction_views.ip_sensor, name='ip_sensor'),
    # path('settings/create/', interaction_views.create),
    # path('settings/edit/<int:sensor_id>/', interaction_views.edit),
    # path('settings/delete/<int:sensor_id>/', interaction_views.delete),
    # re_path(r'^commands/sensor/On|off', interaction_views.sensor, name='sensor'),
    # path('commands/off_sensor/', interaction_views.off_sensor, name='off_sensor'),
    # path('commands/on_sensor/', interaction_views.on_sensor, name='on_sensor'),

    ]