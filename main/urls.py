from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about_us/',views.about,name='about'),
    path('contact_us/', views.ContactUsView.as_view(), name='contact'),
    path('product_list/<slug:tag>',views.product_list, name='product_list'),
    path("product/<slug:slug>/", views.product_detail, name="product"),
    path('add_to_basket/<int:id>',views.add_to_basket,name='add to basket'),
]
