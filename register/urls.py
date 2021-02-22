from django.urls import path, include
from register import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    path('', views.register, name="register"),
    path('profil/',views.profilakun, name="profilakun"),
    path('profil/edit',views.editprofil, name="editprofil"),
    path('admin/', admin.site.urls),
    path('profil/changepassword', views.change_password, name="changepassword"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
