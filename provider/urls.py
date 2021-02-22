from django.urls import path, include
from provider import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.indexprovider, name="indexprovider"),
    path('bukajasa/', views.indexbukajasa, name="bukajasa"),
    path('editbukajasa/', views.editbukajasa, name="editbukajasa"),
    path('posting/', views.indexpostingjasa, name="postingjasa"),
    path('manageposting/', views.indexmanageposting, name="manageposting"),
    path('manageposting/delete/<int:id>', views.indexdeleteposting, name="deleteposting"),
    path('manageposting/edit/<int:id>', views.indexeditposting, name="editposting"),
    path('manageorder/', views.indexmanageorder, name="manageorder"),
    path('manageorder/receivedorder/<str:kode>', views.receivedorder, name="receivedorder"),
    path('manageorder/rejectedorder/<str:kode>', views.rejectedorder, name="rejectedorder"),
    path('manageorder/processorder/<str:kode>', views.processedorder, name="processedorder"),
    path('manageorder/deleteorder/<str:kode>', views.deleteorder, name="deleteorder"),
    path('manageorder/details/<str:kode>', views.detailorder, name="detailorder"),
    path('keluar/', views.keluar, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
