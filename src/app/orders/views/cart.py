from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.orders.schema import CartSchema
from app.orders.logics.cart import CartService  
from core.utils import Response
from core.resources.jwt import JWTClient  


class CartController(Resource):
    def __init__(self):
        self.cart_service = CartService()
        self.jwt_client = JWTClient()
        self.cart_schema = CartSchema(many=True)

    @jwt_required()
    def get(self):
        jwt_identity = get_jwt_identity()
        user_id = self.jwt_client.get_user_id(jwt_identity)

        carts = self.cart_service.get_all(user_id)
        serialized_carts = self.cart_schema.dump(carts)

        return Response(
            success=True, 
            message="Carts returned", 
            data=serialized_carts, 
            status_code=200
        )

    @jwt_required()
    def post(self):
        jwt_identity = get_jwt_identity()
        user_id = self.jwt_client.get_user_id(jwt_identity)
        cart_id = self.cart_service.create(user_id)

        return Response(
            success=True, 
            message="Cart created", 
            data={"cart_id": cart_id}, 
            status_code=201
        )


class CartDetailController(Resource):
    def __init__(self):
        self.cart_service = CartService()
        self.cart_schema = CartSchema()

    @jwt_required()
    def get(self, cart_id):
        cart = self.cart_service.get(cart_id)
        serialized_cart = self.cart_schema.dump(cart)

        return Response(
            success=True, 
            message="Cart returned", 
            data=serialized_cart, 
            status_code=200
        )
