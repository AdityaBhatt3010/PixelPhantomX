import cv2
import utilities

if __name__ == "__main__":
    input_path = input("Enter the input image path: ").strip()
    output_path = input("Enter the output image path (without extension): ").strip() + ".jpg"

    noise_level = input("Select noise level (Min/Max): ").strip().capitalize()
    if noise_level not in ["Min", "Max"]:
        noise_level = "Min"

    watermark_text = input("Enter watermark text (Default: Protected): ").strip()
    if not watermark_text:
        watermark_text = "Protected"

    image = cv2.imread(input_path)
    image = utilities.apply_disruptive_noise(image, noise_level)
    image = utilities.apply_color_shift(image, noise_level)
    image = utilities.apply_visible_watermark(image, watermark_text)
    image = utilities.apply_hidden_watermark(image, watermark_text)
    image = utilities.apply_edge_masking(image, noise_level)

    cv2.imwrite(output_path, image)
    utilities.apply_metadata_poisoning(output_path)

    print(f"\n🔥 All image poisoning techniques applied successfully! Final image saved as: {output_path}")
