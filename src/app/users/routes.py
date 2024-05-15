from app.users.auth_controller import AuthController


def init_auth_routes(api):
    api.add_resource(AuthController, "/v1/auth/login")