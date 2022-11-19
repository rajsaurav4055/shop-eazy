from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<str:category>',views.category_homepage, name='category_homepage'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    #path('homepage', views.homepage, name="homepage"),
    path('product', views.product, name='product'),
    path('order', views.order, name='order'),
    path('cart', views.cart, name='cart'),
    path('signout', views.signout, name='signout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG: #add this
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)