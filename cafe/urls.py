from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import SignupView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Order Management URLs
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/edit/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path('pay/', views.pay_section, name='pay_section'),

    path('login/', auth_views.LoginView.as_view(template_name='cafe/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),

]
