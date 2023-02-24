from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.ProductsHome.as_view(), name='home'),
    path('products/', views.ProductsPage.as_view(), name='products'),
    path('products/category/<slug:cat_slug>', cache_page(30)(views.ProductsCategory.as_view()), name='category'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),

]
