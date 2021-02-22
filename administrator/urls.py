from django.urls import path, include
from administrator import views
from django.conf import settings
from django.conf.urls.static import static
from administrator import views
urlpatterns = [
    path('', views.indexadmin, name="indexadmin"),
    path('managepengguna/', views.indexmanagepengguna, name="managepengguna"),
    path('managereport/', views.indexmanagereport, name="managereport"),
    path('manageorder/', views.reportorder, name="reportorder"),
    path('manageorder/detail/<str:kode>', views.detailorderreport, name="detailorderreport"),    
    path('managereport/received/<int:kode>', views.receivedreport, name="receivedreport"),
    path('managereport/rejected/<int:kode>', views.rejectedreport, name="rejectedreport"),
    path('managereport/delete/<int:kode>', views.deletereport, name="deletereport"),
    path('managereport/cek/<str:path>', views.cek, name="cek"),
    path('accountbanned/<str:nomer>', views.accountbanned, name="accountbanned"),
    path('logout/', views.keluar, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
