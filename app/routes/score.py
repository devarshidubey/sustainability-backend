from flask import request, jsonify, Blueprint
from app import db
from app.models.product import Product
from app.services.scoring import calculate_sustainability_score
from app.services.openai_suggestions import generate_ai_suggestions
from app.utils.validation import validate_product_input

bp = Blueprint("score_bp", __name__)

@bp.route("/score", methods=["POST"])
def score_product():
    #INPUT VALIDATION!!

    raw_data = request.get_json()

    data, errors = validate_product_input(raw_data)
    if errors:
        return jsonify({"errors": errors}), 400

    score, rating = calculate_sustainability_score(data)
    suggestions = generate_ai_suggestions(data)

    product = Product(
        product_name=data["product_name"],
        materials=",".join(data["materials"]),
        weight_grams=data["weight_grams"],
        transport=data["transport"],
        packaging=data["packaging"],
        gwp=data["gwp"],
        cost=data["cost"],
        circularity=data["circularity"],
        sustainability_score=score,
        rating=rating
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "product_name": data["product_name"],
        "sustainability_score": score,
        "rating": rating,
        "suggestions": suggestions,
    })