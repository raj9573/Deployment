from django.urls import path

from app.views import Test

urlpatterns =  [
    path('test-url/',Test.as_view(),name='test-url')
]