import hmac
import hashlib

from django.utils.encoding import force_bytes


def hmac_sha512(key, message):
    return hmac.new(force_bytes(key), force_bytes(message), hashlib.sha512)
