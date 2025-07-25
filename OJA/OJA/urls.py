from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls")),
    path("items/", include("item.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("inbox/", include("conversation.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # NEVER DO THIS IN PROD!!!! 😱
