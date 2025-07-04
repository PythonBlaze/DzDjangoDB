from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.phone_detail, name='phone_detail'),
    path('admin/', admin.site.urls),
]
