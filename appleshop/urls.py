# ================== appleshop URL Configuration ===============

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.forms import CustomLoginForm, CustomPasswordResetForm, CustomSetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('super_admin/', include('super_admin.urls', namespace = 'super_admin')),
    path('', include('home.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('offers/', include('offers.urls', namespace='offers')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('products/', include('products.urls', namespace='products')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('account/', include('account.urls', namespace='account')),

    path('password_reset/', auth_views.PasswordResetView.as_view
    (template_name = 'user/password_reset.html', form_class = CustomPasswordResetForm), name = 'password_reset'),
    path('password_rest_done/', auth_views.PasswordResetDoneView.as_view
    (template_name = 'user/password_reset_done.html'), name = 'password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
    (template_name = 'user/password_reset_confirm.html', form_class = CustomSetPasswordForm), name = 'password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view
    (template_name = 'user/password_reset_complete.html'), name = 'password_reset_complete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
