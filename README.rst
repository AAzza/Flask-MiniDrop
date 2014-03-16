Flask-MiniDrop
______________

This is trivial wrapper around creation of DropboxAPI client just to simplify configuration.
Its aim is to perform connection to predefined dropbox account with already obtained
access_token.

It's toy extension and possibly not you are looking for. There is cool
Flask extension for Dropbox, which supports all required features.
For example: https://github.com/playpauseandstop/Flask-Dropbox

You can easily live without my extension by just using the function::

    from flask import g, current_app
    import dropbox

    def get_dropbox():
        if not has_attr(g, 'dropbox'):
            access_token = current_app.config('DROPBOX_ACCESS_TOKEN')
            g.dropbox = dropbox.client.DropboxClient(access_token)
        return g.dropbox


Usage
+++++

If you want, you can use the extension like this::

    from flask import Flask
    from flask.ext.minidrop import Dropbox

    app = Flask(__name__)
    dropbox = Dropbox(app)
    # you can do dropbox.init_app(app) later if you use factory pattern

    @app.route('/')
    def index():
        # use dropbox client here
        # ...
        dropbox.client.metadata('/')

        return "Hello"

Configuration
+++++++++++++

The extension uses a config value `DROPBOX_ACESS_TOKEN` to get the access_token.
If you need to connect to several dropbox accounts you can specify prefix for
config value, like this::

    # config key DROPBOX1_ACCESS_TOKEN
    dropbox1 = Dropbox(app, prefix='DROPBOX1')

    # config key DROPBOX2_ACCESS_TOKEN
    dropbox2 = Dropbox()
    dropbox.init_app(app, prefix='DROPBOX2')
