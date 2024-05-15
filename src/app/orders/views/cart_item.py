from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.orders.schema import CartItemSchema
from app.orders.logics.cart_item import CartItemService
from core.utils import Response


class CartItemController(Resource):
    def __init__(self):
        self.cart_item_service = CartItemService()
        self.cart_item_schema = CartItemSchema()
        self.cart_items_schema = CartItemSchema(many=True)

    @jwt_required()
    def get(self, cart_id):
        cart_items = self.cart_item_service.get_all(cart_id)
        cart_items_serialized = self.cart_items_schema.dump(cart_items)
        return Response(
            success=True,
            message="Cart items retrieved successfully",
            data=cart_items_serialized,
            status_code=200,
        )

    @jwt_required()
    def post(self, cart_id):
        cart_item_data = self.cart_item_schema.load(request.json)
        self.cart_item_service.create(cart_id, cart_item_data)
        return Response(
            success=True,
            message="Cart item added successfully",
            status_code=201,
        )


class CartItemDetailController(Resource):
    def __init__(self):
        self.cart_item_service = CartItemService()
        self.cart_item_schema = CartItemSchema()

    @jwt_required()
    def get(self, cart_id, cart_item_id):
        cart_item = self.cart_item_service.get(cart_id, cart_item_id)
        cart_item_serialized = self.cart_item_schema.dump(cart_item)
        return Response(
            success=True,
            message="Cart item retrieved successfully",
            data=cart_item_serialized,
            status_code=200,
        )

    @jwt_required()
    def put(self, cart_id, cart_item_id):
        cart_item_data = self.cart_item_schema.load(request.json)
        self.cart_item_service.update(cart_id, cart_item_id, cart_item_data)
        return Response(
            success=True,
            message="Cart item updated successfully",
            status_code=200,
        )

    @jwt_required()
    def delete(self, cart_id, cart_item_id):
        self.cart_item_service.delete(cart_id, cart_item_id)
        return Response(
            success=True,
            message="Cart item deleted successfully",
            status_code=200,
        )
