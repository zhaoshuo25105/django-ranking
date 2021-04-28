
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"01-test$",test_views),
    url(r'02-tmp2',tmp_views, name='tmp2'),
    url(r'03-tmp',change_score),
    url(r'04-tmp',select_views,name='select'),
    url(r'05-tmp',show_views,name='show')
]





