from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^subjects/$', views.SubjectList.as_view()),
    url(r'^subjects/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
