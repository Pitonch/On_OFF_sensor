from django.urls import path, re_path
from interaction import views as interaction_views
from users import views as user_views
from users import views as user_views
from django.contrib.auth import views as auth_views

# POST
# /interaction/

urlpatterns = [
    path('about/', interaction_views.about, name='url_to_about'),
    path('settings/', interaction_views.settings, name='url_to_settings'),
    path('allsensors/', interaction_views.show_sensors, name='all_sensors'),
    path('commands/<ip_sensor>', interaction_views.ip_, name='ip_sensor'),
    path('commands/<ip_sensor>/<status_sensor>', interaction_views.sensor_on_off, name='status_On_Off'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('create/', interaction_views.create, name='create guest'),
    path('index/', interaction_views.index),
    path('showguest/', interaction_views.show_guest, name='show_guest'),
    path('guestlocation/', interaction_views.show_guest_location, name='guest_location'),





    # path('commands/<status>', interaction_views.sensor_on_off, name='status'),

    # path('settings/create/', interaction_views.create),
    # path('settings/edit/<int:sensor_id>/', interaction_views.edit),
    # path('settings/delete/<int:sensor_id>/', interaction_views.delete),
    # re_path(r'^commands/sensor/On|off', interaction_views.sensor, name='sensor'),
    # path('commands/off_sensor/', interaction_views.off_sensor, name='off_sensor'),
    # path('commands/on_sensor/', interaction_views.on_sensor, name='on_sensor'),

    ]