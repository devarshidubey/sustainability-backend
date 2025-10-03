from openai import OpenAI
import os   

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_suggestions(product):

    product_str = "\n".join([f"{k}: {v}" for k, v in product.items()])
    print(product_str)
    
    prompt = f"""
    You are a sustainability consultant AI.
    Analyze the following product and provide 3-5 actionable suggestions to improve its sustainability:

    {product_str}

    Suggestions should be short, clear, and practical.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150
        )
        suggestions_text = response.choices[0].message.content.strip()

        suggestions = [s.strip("-• \n") for s in suggestions_text.split("\n") if s.strip()]
        return suggestions

    except Exception as e:
        print(e)
        return ["Use fewer plastics", "Consider eco-friendly transport", "Improve packaging"]
