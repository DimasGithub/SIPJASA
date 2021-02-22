from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from order import views
urlpatterns = [
    path('<int:id>', views.indexdetails, name="details"),
    path('ulasan/<int:id>', views.ulasan, name="indexulasan"),
    path('detailsjasa/<int:id>', views.indexdetailsjasa, name="indexdetailsjasa"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
