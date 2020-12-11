from django.urls import path
from Tienda import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('products/<str:id>/', views.products, name="products"),
    path('warehouse/', views.warehouse, name="warehouse"),
    path('warehouse/create/', views.createProduct, name="createP"),
    path('warehouse/edit/<str:pk>/', views.editProduct, name="editP"),
    path('warehouse/delete/<str:pk>/', views.deleteProduct, name="deleteP"),
    path('user/login/', views.loginPage, name="login"),
    path('user/logout/', views.logoutPage, name="logout"),
    path('user/register/', views.registerPage, name="register"),
]