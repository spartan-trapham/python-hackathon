from starlette.types import ASGIApp, Scope, Receive, Send
from starlette.authentication import AuthCredentials


class AuthenticationMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        auth_scopes = []
        user = {'is_authenticated': False}

        scope['auth'] = AuthCredentials(auth_scopes)
        scope['user'] = user
        await self.app(scope, receive, send)
