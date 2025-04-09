import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import piexif
import random

# ✅ Adversarial noise for image protection (Inspired by Glaze)
def apply_adversarial_noise(image, noise_level="Min"):
    noise_intensity = 1 if noise_level == "Min" else 5
    noise = np.random.normal(0, noise_intensity, image.shape).astype(np.float32)
    return np.clip(image.astype(np.float32) + noise, 0, 255).astype(np.uint8)

# ✅ Subtle color-space perturbation for AI resistance (Inspired by Nightshade)
def apply_color_perturbation(image, noise_level="Min"):
    intensity = (-2, 2) if noise_level == "Min" else (-5, 5)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    a = np.clip(a + np.random.randint(*intensity, a.shape), 0, 255)
    b = np.clip(b + np.random.randint(*intensity, b.shape), 0, 255)
    return cv2.cvtColor(cv2.merge([l, a.astype(np.uint8), b.astype(np.uint8)]), cv2.COLOR_LAB2BGR)

# ✅ Visible watermark for protection
def apply_watermark(image, text="Protected"):
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    width, height = pil_image.size
    font = ImageFont.load_default()
    position = (width - 100, height - 30)
    draw.text(position, text, fill=(255, 255, 255))
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

# ✅ Invisible watermark (LSB Steganography, randomized pixels)
def apply_invisible_watermark(image, secret_message="Protected"):
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    height, width, _ = image.shape
    total_pixels = height * width
    random.seed(42)
    pixel_indices = random.sample(range(total_pixels), len(binary_message))

    index = 0
    for pos in pixel_indices:
        x, y = divmod(pos, width)
        if index < len(binary_message):
            image[x, y, 2] = (image[x, y, 2] & 254) | int(binary_message[index])  # Modify Blue channel
            index += 1
    return image

# ✅ Edge distortion for AI disruption (Inspired by Nightshade)
def apply_edge_distortion(image, noise_level="Min"):
    lower, upper = (80, 120) if noise_level == "Min" else (50, 150)
    edges = cv2.Canny(image, lower, upper)
    blurred_edges = cv2.GaussianBlur(edges, (3, 3), 0)
    weight = 0.15 if noise_level == "Min" else 0.3
    return cv2.addWeighted(image, 0.85, cv2.cvtColor(blurred_edges, cv2.COLOR_GRAY2BGR), weight, 0)

# ✅ Metadata poisoning for AI misdirection
def apply_metadata_poisoning(image_path):
    exif_dict = {
        "0th": {piexif.ImageIFD.Artist: "Anonymous".encode("utf-8")},
        "Exif": {piexif.ExifIFD.UserComment: "Random Image - Not for AI Training".encode("utf-8")},
        "GPS": {
            piexif.GPSIFD.GPSLatitude: ((37, 1), (46, 1), (59, 1)),
            piexif.GPSIFD.GPSLongitude: ((122, 1), (25, 1), (36, 1))
        },
        "Interop": {},
        "1st": {},
        "thumbnail": None
    }

    exif_bytes = piexif.dump(exif_dict)

    img = Image.open(image_path)
    if img.format != "JPEG":
        image_path = image_path.rsplit(".", 1)[0] + ".jpg"
        img = img.convert("RGB")
        img.save(image_path, "jpeg")

    piexif.insert(exif_bytes, image_path)
    print(f"✅ Metadata poisoning applied: {image_path}")

# ✅ Main execution
if __name__ == "__main__":
    input_path = input("Enter the input image path: ").strip()
    output_path = input("Enter the output image path (without extension): ").strip() + ".jpg"

    # Ask user for noise level
    noise_level = input("Select noise level (Min/Max): ").strip().capitalize()
    if noise_level not in ["Min", "Max"]:
        print("⚠️ Invalid choice! Defaulting to 'Min'.")
        noise_level = "Min"

    # Ask user for watermark text
    watermark_text = input("Enter watermark text (leave blank for default 'Protected'): ").strip()
    if not watermark_text:
        watermark_text = "Protected"

    # Read image and apply transformations
    image = cv2.imread(input_path)
    image = apply_adversarial_noise(image, noise_level)
    image = apply_color_perturbation(image, noise_level)
    image = apply_watermark(image, watermark_text)
    image = apply_invisible_watermark(image, watermark_text)
    image = apply_edge_distortion(image, noise_level)

    cv2.imwrite(output_path, image)
    apply_metadata_poisoning(output_path)

    print(f"\n🔥 All image poisoning techniques applied successfully! Final image saved as: {output_path}")
