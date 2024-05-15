from flask import request
from flask_restful import Resource

from app.users.login_schema import LoginResponseSchema, LoginSchema
from app.users.logics.session_token import SessionTokenService
from core.utils.utils import Response

class AuthController(Resource):
    token_service = SessionTokenService()

    def post(self):
        request_schema = LoginSchema()
        data = request_schema.load(request.json)
        token = self.token_service.generate_token(data)

        response_schema = LoginResponseSchema()
        token = response_schema.dump(token)

        return Response(
            success=True, message="Login Successful", data=token, status_code=200
        )