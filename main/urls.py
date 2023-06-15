from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about_us/',views.about,name='about'),
    path('contact_us/', views.ContactUsView.as_view(), name='contact'),
    path('products/<slug:tag>',views.product_list,name='products')
]
