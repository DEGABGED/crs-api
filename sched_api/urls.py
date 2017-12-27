from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from sched_api import views

urlpatterns = [
    url(r'^subjects/$', views.subject_list),
    url(r'^subjects/(?P<pk>[0-9]+)/$', views.subject_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
