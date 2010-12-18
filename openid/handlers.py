from tipfy import RequestHandler, Response
from tipfy.auth import user_required
from tipfy.auth.openid import OpenIdMixin
from tipfyext.jinja2 import Jinja2Mixin

class BaseHandler( RequestHandler, Jinja2Mixin ):
    pass

class HomeHandler( BaseHandler ):
    def get( self, **kwargs ):
        return self.render_response( 'home.htm' )

class LoginHandler( BaseHandler ):
    def get( self, **kwargs ):
        return self.render_response( 'login.htm' )

class OpenIDHandler( BaseHandler, OpenIdMixin ):
    def get( self, **kwargs ):
        endpoint = self.request.args.get( 'openid_identifier', None )

        if self.request.args.get( 'openid.mode', None ):
            # If 'openid.mode' is in the URL, this may be a user redirected
            # after an authentication attempt. Try to get the user info and
            # set self._on_auth() as a callback. It will be called passing
            # a dictionary of user info or None if the auntentication is not
            # valid.
            return self.get_authenticated_user( self._on_auth, openid_endpoint=endpoint )

        # Redirect to the OpenId provider to authenticate the user.
        #return Response( '<pre>%s</pre>' % endpoint )
        return self.authenticate_redirect( openid_endpoint=endpoint )

    def _on_auth( self, user ):
        if not user:
            self.abort( 403 )

        return Response( str(user) )

class ProtectedHandler( BaseHandler ):
    @user_required
    def get( self, **kwargs ):
        pass
