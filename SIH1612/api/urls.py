from django.contrib import admin
from django.urls import path, include
from UserManagementApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include("api.urls")),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]



