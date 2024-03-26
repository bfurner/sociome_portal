from django.urls import path, include
from globus_portal_framework.views import search,search_about

urlpatterns = [
    # Provides the basic search portal
    path('', search_about, {"index": "sociome"}),
    path('<index>/data', search, name='search'),
    path('', include('globus_portal_framework.urls')),
    # Provides Login urls for Globus Auth
    path('', include('social_django.urls', namespace='social')),
]