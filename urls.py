# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy import Rule

rules = [
    Rule('/', name='home', handler='openid.handlers.HomeHandler'),
    Rule('/login', name='auth/login', handler='openid.handlers.LoginHandler'),
    Rule('/auth/openid', name='auth/openid', handler='openid.handlers.OpenIDHandler'),
    Rule('/protected', name='protected', handler='openid.handlers.ProtectedHandler'),
]
