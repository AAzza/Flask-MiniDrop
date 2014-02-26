# coding: utf-8
__author__ = 'Nataliia Uvarova'
__license__ = 'BSD License'
__version__ = '0.1'

import dropbox
from flask import current_app

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

__all__ = ('Dropbox', )


DEFAULT_PREFIX = 'DROPBOX'
CONFIG_KEY = '_ACCESS_TOKEN'
CTX_KEY = '_CLIENT'


class Dropbox(object):
    def __init__(self, app=None, prefix=DEFAULT_PREFIX):
        self.app = app
        if app is not None:
            self.init_app(app, prefix)

    def init_app(self, app, prefix=DEFAULT_PREFIX):
        self.prefix = prefix

    @property
    def client(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, self.prefix + CTX_KEY):
                access_token = current_app.config[self.prefix + CONFIG_KEY]
                client = dropbox.client.DropboxClient(access_token)
                setattr(ctx, self.prefix + CTX_KEY, client)
            return getattr(ctx, self.prefix + CTX_KEY)
