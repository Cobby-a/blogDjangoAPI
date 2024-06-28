from django.urls import path


from .views import SettingsView
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('settings', SettingsView.as_view()),
    path('create-new-setting/', SettingsView.as_view()),
]