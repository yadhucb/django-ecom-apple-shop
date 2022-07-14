from django.urls import path
from profiles import views
app_name = 'profiles'
urlpatterns = [
    path('customer_profile/', views.CustomerProfileView.as_view(), name = 'customer_profile'),
    path('admin_profile/', views.AdminProfileView.as_view(), name = 'admin_profile'),
    path('address/', views.addressView, name = 'address'),
    path('address_delete/', views.addressDeleteView, name = 'address_delete'),
    path('address_edit/', views.addressEdit, name = 'address_edit'),
    path('address_default/', views.addressDefaultView, name = 'address_dafault'),
]
