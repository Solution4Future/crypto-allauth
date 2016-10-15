import base64
import hashlib

import datetime
import uuid

import binascii

import bitcoin
from allauth.socialaccount import providers
from allauth.socialaccount.helpers import render_authentication_error, complete_social_login
from allauth.socialaccount.models import SocialLogin
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.utils.encoding import force_bytes
from django.views.generic import TemplateView

from .provider import TrezorProvider


def verify(challenge_hidden, challenge_visual, pubkey, signature, version):
    version = int(version)
    if version == 1:
        message = binascii.unhexlify(challenge_hidden + binascii.hexlify(challenge_visual))
    elif version == 2:
        h1 = hashlib.sha256(binascii.unhexlify(challenge_hidden)).digest()
        h2 = hashlib.sha256(challenge_visual).digest()
        message = h1 + h2
    else:
        raise Exception('Unknown version')
    signature_b64 = base64.b64encode(binascii.unhexlify(signature))
    return bitcoin.ecdsa_verify(message, signature_b64, pubkey)


class TrezorLoginView(TemplateView):
    template_name = 'trezor/trezor_connect.html'

    def get(self, request, *args, **kwargs):
        trezor_data = {
            'challenge_hidden': hashlib.sha512(uuid.uuid4().bytes).hexdigest(),
            'challenge_visual': str(datetime.datetime.utcnow()),
        }
        request.session['trezor_data'] = trezor_data
        ctx = {'trezor_data': trezor_data, 'callback': reverse('trezor_login')}
        return self.render_to_response(ctx)

    def post(self, request, *args, **kwargs):
        trezor_data = request.session['trezor_data']
        extra_data = {
            'public_key': request.POST.get('public_key'),
            'signature': request.POST.get('signature'),
            'version': request.POST.get('version'),
        }

        is_ok = verify(trezor_data['challenge_hidden'],
                       force_bytes(trezor_data['challenge_visual']),
                       extra_data['public_key'],
                       extra_data['signature'],
                       extra_data['version'])

        if not is_ok:
            return render_authentication_error(request, provider_id=TrezorProvider.id)

        login = providers.registry.\
            by_id(TrezorProvider.id, request).\
            sociallogin_from_response(request, extra_data)

        login.state = SocialLogin.state_from_request(request)
        return complete_social_login(request, login)
