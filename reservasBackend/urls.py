from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Vehicles.views import VehicleListView, OfficeListView, get_available_models



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentication/', include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    path('api/vehicles/', VehicleListView.as_view(), name='vehicle-list'),
    path('api/offices/', OfficeListView.as_view(), name='Office-list'),
    path('api/get_available_models/', get_available_models, name='get_available_models'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

