from app.products.views.products import ProductController, ProductDetailController
from app.products.views.product_label import (
    ProductLabelController,
    ProductLabelDetailController,
)


def init_product_routes(api):
    api.add_resource(ProductController, "/v1/products")
    api.add_resource(ProductDetailController, "/v1/products/<int:product_id>")
    api.add_resource(ProductLabelController, "/v1/products/<int:product_id>/labels")
    api.add_resource(
        ProductLabelDetailController,
        "/v1/products/<int:product_id>/labels/<int:label_id>",
    )
