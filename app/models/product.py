from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    materials = db.Column(db.String(200), nullable=False)  # store as comma-separated string
    weight_grams = db.Column(db.Float, nullable=False)
    transport = db.Column(db.String(50), nullable=False)
    packaging = db.Column(db.String(50), nullable=False)
    gwp = db.Column(db.Float, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    circularity = db.Column(db.Float, nullable=False)
    sustainability_score = db.Column(db.Float)
    rating = db.Column(db.String(2))

    def to_dict(self):
        return {
            "product_name": self.product_name,
            "materials": self.materials.split(","),
            "weight_grams": self.weight_grams,
            "transport": self.transport,
            "packaging": self.packaging,
            "gwp": self.gwp,
            "cost": self.cost,
            "circularity": self.circularity,
            "sustainability_score": self.sustainability_score,
            "rating": self.rating
        }
