from PIL import Image
import io
import os

def remove_background(image_path: str) -> Image.Image:
    # Import rembg's remove function with pymatting/numba disabled
    # This avoids the numba JIT compilation error on Python 3.14
    from rembg.bg import remove
    
    with open(image_path, "rb") as f:
        input_data = f.read()
    output_data = remove(
        input_data,
        alpha_matting=False,  # disable pymatting (requires numba, broken on 3.14)
    )
    image = Image.open(io.BytesIO(output_data)).convert("RGBA")
    return image

def save_no_bg(image: Image.Image, output_path: str):
    image.save(output_path, "PNG")
    print(f"Saved transparent image: {output_path}")
