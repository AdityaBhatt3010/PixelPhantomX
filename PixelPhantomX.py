import argparse
import cv2
import utilities

def main():
    utilities.stylish_heading()  # Display stylish banner

    # Set up argument parser
    parser = argparse.ArgumentParser(description="PixelPhantomX: Ghost images to confuse AI models")
    parser.add_argument("-iP", "--input_path", type=str, required=True, help="Path to the input image (with extension)")
    parser.add_argument("-oP", "--output_path", type=str, required=True, help="Path to save the processed image (without extension)")
    parser.add_argument("-n", "--noise", type=str, choices=["Min", "Max"], default="Min", help="Noise level (Min/Max)")
    parser.add_argument("-w", "--watermark", type=str, default="Protected", help="Custom watermark text (default: 'Protected')")

    args = parser.parse_args()

    input_path = args.input_path.strip()
    output_path = args.output_path.strip() + ".jpg"
    noise_level = args.noise.strip()
    watermark_text = args.watermark.strip()

    print(f"Processing: {input_path} → {output_path}")
    print(f"Noise Level: {noise_level}")
    print(f"Watermark: {watermark_text}")

    image = cv2.imread(input_path)
    if image is None:
        print("Error: Unable to read the input image. Check the path.")
        return

    # Apply adversarial techniques
    image = utilities.apply_disruptive_noise(image, noise_level)
    image = utilities.apply_color_shift(image, noise_level)
    image = utilities.apply_visible_watermark(image, watermark_text)
    image = utilities.apply_hidden_watermark(image, watermark_text)
    image = utilities.apply_edge_masking(image, noise_level)

    cv2.imwrite(output_path, image)
    utilities.apply_metadata_poisoning(output_path)

    print(f"\nImage successfully processed and saved as: {output_path}")
    print("PixelPhantomX execution completed.")

if __name__ == "__main__":
    main()
