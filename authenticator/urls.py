from django.urls import path
from authenticator import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('signup', views.signup, name="signup"),
    path('login', views.handleLogin, name="handlelogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    path('contact', views.contact, name="contact"),
    path('join', views.enroll, name="enroll"),
    path('profile', views.profile, name="profile"),
    path('gallery', views.gallery, name="gallery"),
    path('attendance', views.attendance, name="attendance"),

]
