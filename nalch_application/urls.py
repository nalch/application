from django.conf.urls import url

from views import (
    contact,
    index,
    references
)


urlpatterns = [
    url(r'^(?P<applicant>[a-z]+)/$', index, name='index'),
    url(r'^(?P<applicant>[a-z]+)/references/$', references, name='references'),
    url(r'^(?P<applicant>[a-z]+)/contact/$', contact, name='contact')
]
