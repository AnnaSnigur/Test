from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from profile_app import views

app_name = 'profile_app'

urlpatterns = [
     path('admin/', admin.site.urls),
     path('signup/', views.SignUp.as_view(), name='signup'),
     path('profile/<int:pk>/', views.MyProfile.as_view(), name='my_profile'),
     path('edit-profile/<int:pk>/', views.EditProfile.as_view(), name='edit_profile'),
     path('login/', views.Login.as_view(), name='login'),
]
