from django.conf.urls import url

from . import views

urlpatterns = [
    url('^trezor/login/$', views.TrezorLoginView.as_view(), name="trezor_login")
]
