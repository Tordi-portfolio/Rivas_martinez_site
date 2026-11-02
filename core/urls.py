from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("portal/login/", views.PortalLogin.as_view(), name="portal_login"),
    path("portal/logout/", LogoutView.as_view(), name="portal_logout"),
    path("portal/", views.dashboard, name="portal_dashboard"),
    path("portal/message/<int:pk>/", views.message_detail, name="portal_message"),
    path("portal/message/<int:pk>/action/", views.message_action, name="portal_action"),
]
