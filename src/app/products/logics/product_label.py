from app.products.models import ProductLabel
from app.products.logics.product import ProductService
from core.error_handlers import AppError
from core.utils.utils import BaseService


class ProductLabelService(BaseService):
    model = ProductLabel

    def __init__(self):
        self.product_service = ProductService()

    def create(self, product_id, data):
        self.product_service.get(product_id)
        
        label = self.model(**data, product_id=product_id)
        try:
            label.save()
        except Exception as e:
            self.logger.error(f"ProductLabelService.create(): {str(e)}")
            raise AppError(500, "Failed to create product label")

    def get_all(self, product_id):
        try:
            labels = self.model.query.filter_by(product_id=product_id).all()
        except Exception as e:
            self.logger.error(f"ProductLabelService.get_all(): {str(e)}")
            raise AppError(500, "Failed to retrieve product labels")

        return labels

    def get(self, product_id, label_id):
        try:
            label = self.model.query.filter_by(product_id=product_id, id=label_id).first()
        except Exception as e:
            self.logger.error(f"ProductLabelService.get(): {str(e)}")
            raise AppError(500, "Failed to retrieve product label")

        if not label:
            raise AppError(404, "Product label not found")

        return label

    def update(self, product_id, label_id, data):
        label = self.get(product_id, label_id)

        try:
            label.update(data)
        except Exception as e:
            self.logger.error(f"ProductLabelService.update(): {str(e)}")
            raise AppError(500, "Failed to update product label")

    def delete(self, product_id, label_id):
        label = self.get(product_id, label_id)
        try:
            label.delete()
        except Exception as e:
            self.logger.error(f"ProductLabelService.delete(): {str(e)}")
            raise AppError(500, "Failed to delete product label")
