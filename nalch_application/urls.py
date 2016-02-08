from django.conf.urls import url

from views import (
    areasofexpertise,
    areasofinterest,
    contact,
    index,
    references
)


urlpatterns = [
    url(r'^(?P<applicant>[a-z]+)/$', index, name='index'),
    url(r'^(?P<applicant>[a-z]+)/references/$', references, name='references'),
    url(r'^(?P<applicant>[a-z]+)/contact/$', contact, name='contact'),
    url(r'^(?P<applicant>[a-z]+)/areasofinterest/$', areasofinterest, name='areasofinterest'),
    url(r'^(?P<applicant>[a-z]+)/areasofexpertise/$', areasofexpertise, name='areasofexpertise')
]
