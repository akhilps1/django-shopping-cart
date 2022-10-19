from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_details, name='cart_details'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:item_id>/',views.delete_item, name='delete_item'),
    path('delete/<int:item_id>/', views.delete, name='delete')
]