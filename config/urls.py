from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "CODEMATRIX Admin"
admin.site.site_title = "CODEMATRIX"
admin.site.index_title = "Content management"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path('panel/', include('dashboard.urls')),
]

handler404 = "core.views.page_not_found"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
