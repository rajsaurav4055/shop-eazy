from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
     path('', views.homepage, name='homepage'),
     path('category_homepage/<str:category>',views.category_homepage, name='category_homepage'),
     path('signup', views.signup, name='signup'),
     path('signin',views.signin, name='signin'),
     #path('homepage', views.homepage, name="homepage"),
     path('add-to-cart',views.add_to_cart,name='add_to_cart'),
     path('cart',views.cart,name='cart'),
     path('product/<int:id>', views.product, name='product'),
     path('order', views.order, name='order'),
     path('orderlist', views.orderlist, name='orderlist'),
     path('cart', views.cart, name='cart'),
    path('signout', views.signout, name='signout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG: #add this
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)