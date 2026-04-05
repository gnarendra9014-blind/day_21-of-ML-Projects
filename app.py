import os
from remover import remove_background, save_no_bg
from backgrounds import apply_background, apply_custom_color, BACKGROUNDS
from describer import describe_product

def main():
    print("\n=== Product Photo Background Swapper ===")
    print("Remove backgrounds and replace with professional studio backgrounds.\n")

    image_path = input("Enter product image path (JPG or PNG): ").strip().strip('"').strip("'")
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return

    base_name = os.path.splitext(os.path.basename(image_path))[0]

    # Step 1: AI analyzes product
    print("\nAI analyzing your product...")
    description = describe_product(image_path)
    print(f"Product detected: {description['product']}")
    print(f"Style: {description['style']}")
    print(f"Recommended background: {description['recommended_bg']}")
    print(f"Reason: {description['reason']}")

    # Step 2: Remove background
    print("\nRemoving background (this takes 10-30 seconds)...")
    product_no_bg = remove_background(image_path)
    no_bg_path = f"{base_name}_no_background.png"
    save_no_bg(product_no_bg, no_bg_path)

    # Step 3: Choose background
    print("\nAvailable backgrounds:")
    for i, bg in enumerate(BACKGROUNDS.keys()):
        marker = " <-- AI recommended" if bg == description["recommended_bg"] else ""
        print(f"  {i+1}. {bg}{marker}")
    print(f"  {len(BACKGROUNDS)+1}. Custom hex color (e.g. #FF5733)")
    print(f"  {len(BACKGROUNDS)+2}. Generate ALL backgrounds")

    choice = input("\nChoose background number: ").strip()

    bg_list = list(BACKGROUNDS.keys())

    try:
        idx = int(choice) - 1
        if idx == len(BACKGROUNDS):
            hex_color = input("Enter hex color (e.g. #FF5733): ").strip()
            result = apply_custom_color(product_no_bg, hex_color)
            output_path = f"{base_name}_custom_{hex_color.replace('#','')}.jpg"
            result.save(output_path, "JPEG", quality=95)
            print(f"\nSaved: {output_path}")

        elif idx == len(BACKGROUNDS) + 1:
            print("\nGenerating all backgrounds...")
            for bg_name in bg_list:
                result = apply_background(product_no_bg, bg_name)
                output_path = f"{base_name}_{bg_name}.jpg"
                result.save(output_path, "JPEG", quality=95)
                print(f"  Saved: {output_path}")
            print(f"\nAll {len(bg_list)} backgrounds generated!")

        elif 0 <= idx < len(bg_list):
            bg_name = bg_list[idx]
            result = apply_background(product_no_bg, bg_name)
            output_path = f"{base_name}_{bg_name}.jpg"
            result.save(output_path, "JPEG", quality=95)
            print(f"\nSaved: {output_path}")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input.")

    print("\nDone! Your product photos are ready.")

if __name__ == "__main__":
    main()
