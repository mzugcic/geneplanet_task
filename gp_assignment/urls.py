from django.contrib import admin
from django.urls import path, include
from genomes.urls import urlpatterns as genome_urlpatterns

urlpatterns = [
    path('genomes/', include((genome_urlpatterns, 'genomes'), namespace='genomes')),
    path('admin/', admin.site.urls),
]
