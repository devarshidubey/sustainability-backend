from flask import jsonify, Blueprint
from app.models.product import Product
from app.services.openai_summary import generate_top_issues
from collections import Counter

bp = Blueprint("summary_bp", __name__)

@bp.route("/score-summary", methods=["GET"])
def score_summary():
    products = Product.query.all()
    total = len(products)
    avg_score = sum(p.sustainability_score for p in products) / total if total else 0
    ratings_count = Counter(p.rating for p in products)

    top_issues = generate_top_issues(products)

    return jsonify({
        "total_products": total,
        "average_score": round(avg_score, 2),
        "ratings": dict(ratings_count),
        "top_issues": top_issues
    })
