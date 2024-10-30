from django.urls import re_path as url
from .views import usuarioAlumViewSet, usuarioProViewSet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^core/usuarioAlum/$', usuarioAlumViewSet.as_view()),
    url(r'^core/usuarioPro/$', usuarioProViewSet.as_view()), 
]

urlpatterns = format_suffix_patterns(urlpatterns)

