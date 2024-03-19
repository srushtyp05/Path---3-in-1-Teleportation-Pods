from django.urls import path
from . import views
from .views import homepage


app_name = 'PATH'
urlpatterns = [
    # path('login/', views.user_login, name='login'),

    path('', homepage, name='homepage'),
    # path('carrental/',views.home,name='home'),
    path('carrental/contactUs/', views.contact_us, name='contactUs'),
    path('carrental/submitContactInfo/', views.contact_us, name='submitContactInfo'),

    path('carrental/carsInventory/', views.carInventory, name='carsInventory'),
    path('carrental/rentedCars/', views.rentedCars, name='submitContactInfo'),

]
