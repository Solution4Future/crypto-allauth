from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url('^trezor/login/$', csrf_exempt(views.TrezorLoginView.as_view()), name="trezor_login")
]
