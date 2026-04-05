from PIL import Image, ImageDraw, ImageFilter
import os

BACKGROUNDS = {
    "white_studio": (255, 255, 255),
    "soft_gray": (240, 240, 240),
    "dark_studio": (30, 30, 30),
    "navy_blue": (15, 30, 80),
    "forest_green": (20, 80, 40),
    "warm_beige": (245, 235, 220),
    "sky_blue": (135, 206, 235),
    "rose_gold": (212, 175, 155),
}

def create_gradient_bg(width: int, height: int, color1: tuple, color2: tuple) -> Image.Image:
    bg = Image.new("RGBA", (width, height))
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        for x in range(width):
            bg.putpixel((x, y), (r, g, b, 255))
    return bg

def apply_background(product_image: Image.Image, bg_name: str) -> Image.Image:
    width, height = product_image.size

    if bg_name in BACKGROUNDS:
        color = BACKGROUNDS[bg_name]
        if bg_name == "white_studio":
            bg = create_gradient_bg(width, height, (255, 255, 255), (230, 230, 230))
        elif bg_name == "dark_studio":
            bg = create_gradient_bg(width, height, (50, 50, 50), (15, 15, 15))
        elif bg_name == "soft_gray":
            bg = create_gradient_bg(width, height, (250, 250, 250), (220, 220, 220))
        else:
            darker = tuple(max(0, c - 40) for c in color)
            bg = create_gradient_bg(width, height, color, darker)
    else:
        bg = Image.new("RGBA", (width, height), (255, 255, 255, 255))

    bg.paste(product_image, (0, 0), product_image)
    return bg.convert("RGB")

def apply_custom_color(product_image: Image.Image, hex_color: str) -> Image.Image:
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    width, height = product_image.size
    darker = (max(0, r-40), max(0, g-40), max(0, b-40))
    bg = create_gradient_bg(width, height, (r, g, b), darker)
    bg.paste(product_image, (0, 0), product_image)
    return bg.convert("RGB")
