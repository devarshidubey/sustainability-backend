from marshmallow import Schema, fields, validate, ValidationError, EXCLUDE

class WeightsSchema(Schema):
    gwp = fields.Float(required=True, validate=validate.Range(min=0, max=1))
    circularity = fields.Float(required=True, validate=validate.Range(min=0, max=1))
    cost = fields.Float(required=True, validate=validate.Range(min=0, max=1))

class ProductSchema(Schema):
    product_name = fields.String(required=True, validate=validate.Length(min=1))
    materials = fields.List(fields.String(), required=True, validate=validate.Length(min=1))
    weight_grams = fields.Float(required=True, validate=validate.Range(min=0))
    transport = fields.String(required=True, validate=validate.Length(min=1))
    packaging = fields.String(required=True, validate=validate.Length(min=1))
    gwp = fields.Float(required=True, validate=validate.Range(min=0))
    cost = fields.Float(required=True, validate=validate.Range(min=0))
    circularity = fields.Float(required=True, validate=validate.Range(min=0, max=100))
    weights = fields.Nested(WeightsSchema, required=False)

    class Meta:
        unknown = EXCLUDE

def validate_product_input(data):
    schema = ProductSchema()
    try:
        validated_data = schema.load(data) 
        return validated_data, None
    except ValidationError as err:
        return None, err.messages
