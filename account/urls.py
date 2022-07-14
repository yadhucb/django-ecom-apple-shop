from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm, CustomPasswordResetForm, CustomSetPasswordForm
from account import views
app_name = 'account'
urlpatterns = [
    path('send_otp', views.send_otp, name = 'send_otp'),
    path('verify_otp', views.verify_otp, name ='verify_otp'),
    path('create_account/', views.userCreationView, name='create_account' ),
    path('login/', auth_views.LoginView.as_view
    (template_name='user/login.html', authentication_form =CustomLoginForm ,next_page= 'home'), name= 'login' ),
    path('logout/', views.logoutView, name='logout'),
    
    path('admin_login/', auth_views.LoginView.as_view
    (template_name='super_admin/login.html', authentication_form =CustomLoginForm ,next_page= 'super_admin:home'), name= 'admin_login' ),
    path('admin_creation', views.AdminCreationView.as_view(), name='admin_creation'),
    path('admin_logout', views.adminLogoutView, name='admin_logout'),

]
