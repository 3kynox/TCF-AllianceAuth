from django.urls import re_path, include
from django.contrib import admin
import allianceauth.urls

urlpatterns = [
    # Admin
    re_path(r'^admin/', admin.site.urls),
    # AllianceAuth URLs (toutes les routes originales)
    re_path(r'', include(allianceauth.urls)),
]
