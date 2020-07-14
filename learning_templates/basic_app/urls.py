from django.conf.urls import url
from basic_app import views
from django.urls import path
# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    url('other/',views.other,name='other'),
]
