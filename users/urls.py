from django.urls import path
from .views import (loginview, profile, signupview,
                    profile_settings, change_email, logoutview,
                    change_password, profile_search_notes, profile_settings_search_notes)


app_name = 'users'


urlpatterns = [
    path('login/', loginview, name='login'),
    path('signup/', signupview, name='signup'),
    path('profile/', profile, name='profile'),
    path('profile/settings/', profile_settings, name='profile_settings'),
    path('settings/change-email/', change_email, name='change_email'),
    path('settings/change-password/', change_password, name='change_password'),
    path('logout/', logoutview, name='logout'),
    path('profile/search-notes/', profile_search_notes, name='profile_search_notes'),
    path('profile/settings/search-notes/', profile_settings_search_notes, name='profile_settings_search_notes'),

]
