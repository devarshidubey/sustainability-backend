from flask import jsonify, Blueprint
from app.models.product import Product
from collections import Counter

bp = Blueprint("history_bp", __name__)

@bp.route("/history", methods=["GET"])
def history():
    products = Product.query.order_by(Product.id.desc()).limit(20).all()
    return jsonify([
        {"product_name": p.product_name, "sustainability_score": p.sustainability_score, "rating": p.rating}
        for p in products
    ])
