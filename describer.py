import os, base64
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def describe_product(image_path: str) -> dict:
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    ext = image_path.lower().split(".")[-1]
    mime = "jpeg" if ext in ["jpg", "jpeg"] else "png"

    res = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/{mime};base64,{image_data}"}
                },
                {
                    "type": "text",
                    "text": """Analyze this product image and recommend the best background.
Reply in EXACTLY this format:
PRODUCT: what the product is
STYLE: casual or luxury or minimal or bold
RECOMMENDED_BG: best background from: white_studio, soft_gray, dark_studio, navy_blue, forest_green, warm_beige, sky_blue, rose_gold
REASON: one sentence why this background works best"""
                }
            ]
        }],
        max_tokens=150,
    )
    return parse_description(res.choices[0].message.content)

def parse_description(text: str) -> dict:
    result = {"product": "", "style": "", "recommended_bg": "white_studio", "reason": ""}
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("PRODUCT:"):
            result["product"] = line.split(":", 1)[-1].strip()
        elif line.startswith("STYLE:"):
            result["style"] = line.split(":", 1)[-1].strip()
        elif line.startswith("RECOMMENDED_BG:"):
            bg = line.split(":", 1)[-1].strip().lower().replace(" ", "_")
            result["recommended_bg"] = bg
        elif line.startswith("REASON:"):
            result["reason"] = line.split(":", 1)[-1].strip()
    return result
