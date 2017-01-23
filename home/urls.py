from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^books/$', BookList.as_view(), name='bklst'),
    url(r'^books-adv/$', BookAdvancedList.as_view(), name='bklstadv'),
    url(r'^books/(?P<pk>[0-9]+)/$', BookDetail.as_view(), name='bkdtl'),
    url(r'^authors/$', AuthorList.as_view(), name='athlst'),
    url(r'^authors/(?P<pk>[0-9]+)/$', AuthorDetail.as_view(), name='athdtl'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
