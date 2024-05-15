from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.products.schema import ProductLabelSchema
from app.products.logics.product_label import ProductLabelService
from core.utils import Response


class ProductLabelController(Resource):
    def __init__(self):
        self.product_label_service = ProductLabelService()
        self.product_label_schema = ProductLabelSchema()
        self.product_labels_schema = ProductLabelSchema(many=True)

    @jwt_required()
    def get(self, product_id):
        labels = self.product_label_service.get_all(product_id)
        serialized_labels = self.product_labels_schema.dump(labels)
        
        return Response(
            success=True,
            message="All products label retrieved",
            data=serialized_labels,
            status_code=200,
        )

    @jwt_required()
    def post(self, product_id):
        label_data = self.product_label_schema.load(request.json)
        self.product_label_service.create(product_id, label_data)
        
        return Response(
            success=True, 
            message="New product label has been added", 
            status_code=201
        )


class ProductLabelDetailController(Resource):
    def __init__(self):
        self.product_label_service = ProductLabelService()
        self.product_label_schema = ProductLabelSchema()

    @jwt_required()
    def get(self, product_id, label_id):
        label = self.product_label_service.get(product_id, label_id)
        serialized_label = self.product_label_schema.dump(label)
        
        return Response(
            success=True,
            message="Retrieved specific product label",
            data=serialized_label,
            status_code=200,
        )

    @jwt_required()
    def patch(self, product_id, label_id):
        updated_data = self.product_label_schema.load(request.json, partial=True)
        self.product_label_service.update(product_id, label_id, updated_data)
        
        return Response(
            success=True, 
            message="Product label has been updated", 
            status_code=200
        )

    @jwt_required()
    def delete(self, product_id, label_id):
        self.product_label_service.delete(product_id, label_id)
        
        return Response(
            success=True, 
            message="Product label successfully deleted", 
            status_code=200
        )