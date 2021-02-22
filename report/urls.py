from django.urls import path, include
from report import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.indexreport, name="indexreport"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
