from django.urls import path
from interaction import views as interaction_views
from users import views as user_views
from django.contrib.auth import views as auth_views


# POST
# /interaction/

urlpatterns = [
    path('about/', interaction_views.about, name='url_to_about'),
    path('allsensors/', interaction_views.show_sensors, name='all_sensors'),
    path('commands/<ip_sensor>', interaction_views.ip_, name='ip_sensor'),
    path('commands/<ip_sensor>/<status_sensor>', interaction_views.sensor_on_off, name='status_On_Off'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]
