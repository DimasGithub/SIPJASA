from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('peraturan-sistem/', views.indexrule, name="indexrule"),
    path('panduan-sistem/', views.indexguide, name="indexguide"),
    path('kategori/<str:kategori>', views.indexkategori, name="indexkategori"),
    path('banned/', views.indexbanned, name="indexbanned"),
    path('register/',include(('register.urls', 'register'), namespace='register')),
    path('login/',include(('login.urls', 'login'), namespace='login')),
    path('report/', include(('report.urls', 'report'), namespace='report')),
    path('customer/',include(('customer.urls', 'customer'), namespace='customer')),
    path('provider/',include(('provider.urls', 'provider'), namespace='provider')),
    path('administrator/', include(('administrator.urls', 'administrator'), namespace="administrator")),
    path('details/', include(('order.urls', 'order'), namespace='order')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
