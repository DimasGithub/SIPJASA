from django.urls import path, include
from customer import views
urlpatterns = [
    path('', views.indexcustomer, name="indexcustomer"),
    path('cart/', views.indexcart, name="indexcart"),
    path('cart/details/<str:kode>', views.indexcartdetail, name="indexcartdetail"),
    path('cart/edit/<str:kode>', views.indexcartedit, name="indexeditpesanan"),
    path('cart/delete/<str:kode>', views.deletecart, name="deletecart"),
    path('cart/score/<str:kode>', views.finishorder, name="finishorder"),
    path('logout/', views.keluar, name="logout"),
]
