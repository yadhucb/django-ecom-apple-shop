from django.urls import path
from super_admin import views

app_name = 'super_admin'
urlpatterns = [
    path('',views.homeView, name='home'),
    path('chart/',views.homeView, name='home'),

    path('category_add',views.CategoryAddView.as_view(), name='category_add'),
    path('category_list/', views.categoryListView, name= 'category_list'),
    path('category_details/<str:pk>', views.categoryDetailsView, name= 'category_details'),
    path('category_edit/<str:pk>', views.CategoryEditView.as_view(), name= 'category_edit'),
    path('category_delete/<str:pk>', views.categoryDeleteView, name= 'category_delete'),

    path('product_add',views.ProductAddView.as_view(), name='product_add'),
    path('product_list/', views.productListView, name= 'product_list'),
    path('product_details/<str:pk>', views.productDetailsView, name= 'product_details'),
    path('product_edit/<str:pk>', views.ProductEditView.as_view(), name= 'product_edit'),
    path('product_delete/<str:pk>', views.productDeleteView, name= 'product_delete'),

    path('coupon_add',views.couponAddView, name='coupon_add'),
    path('coupon_list/', views.couponListView, name= 'coupon_list'),
    path('coupon_edit/<str:pk>', views.CouponEditView.as_view(), name= 'coupon_edit'),
    path('coupon_delete/<str:pk>', views.couponDeleteView, name= 'coupon_delete'),

    path('order_list/', views.OrderListView.as_view(), name= 'order_list'),

    path('customer_list/', views.customerListView, name= 'customer_list'),
    path('admin_list/', views.adminListView, name= 'admin_list'),
    path('admin_request_list/', views.AdminRequestListView.as_view(), name= 'admin_request_list'),


]



