import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_top_issues(products):

    products_str = ""
    for i, p in enumerate(products, 1):
        products_str += f"- Product {i}: {p.product_name}, Materials: {p.materials}, Transport: {p.transport}, Packaging: {p.packaging}, GWP: {p.gwp}, Cost: {p.cost}, Circularity: {p.circularity}\n"

    prompt = f"""
    You are a sustainability analyst AI.
    Given these products and their properties, identify the 3-5 most common sustainability issues across all products.
    Return the issues as a JSON array of short strings.
    
    Products:
    {products_str}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150
        )
        suggestions_text = response.choices[0].message.content.strip()

        import json
        issues = json.loads(suggestions_text)
        return issues
    except Exception:

        issues = []
        for p in products:
            if "plastic" in p.materials.lower(): issues.append("Plastic used")
            if p.transport.lower() == "air": issues.append("Air transport")
            if p.packaging.lower() not in ["recyclable", "biodegradable"]:
                issues.append("Non-recyclable packaging")

        from collections import Counter
        return [issue for issue, _ in Counter(issues).most_common(5)]
