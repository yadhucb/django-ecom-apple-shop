from django.urls import path
from orders import views
app_name = 'orders'
urlpatterns = [
    path('single_order/<str:pk>/', views.singleOrderView, name = 'single_order'),
    path('cart_order/', views.cartOrderView, name = 'cart_order'),
    path('your_order/', views.yourOrderView, name = 'your_order'),

    path('payment', views.paymentView),
    path('razorpay/', views.razorpayKey)

]
