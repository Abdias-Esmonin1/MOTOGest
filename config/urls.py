from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core import views as core_views

urlpatterns = [
    path('manifest.webmanifest', core_views.manifest, name='manifest'),
    path('service-worker.js', core_views.service_worker, name='service_worker'),
    path('offline/', core_views.offline, name='offline'),
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('motos/', include('apps.motos.urls')),
    path('conducteurs/', include('apps.conducteurs.urls')),
    path('paiements/', include('apps.paiements.urls')),
    path('pannes/', include('apps.pannes.urls')),
    path('maintenance/', include('apps.maintenance.urls')),
    path('finances/', include('apps.finances.urls')),
    path('rapports/', include('apps.rapports.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
