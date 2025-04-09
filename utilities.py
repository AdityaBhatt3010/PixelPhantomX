import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import piexif
import random
from pyfiglet import figlet_format
from termcolor import colored

# ✅ Stylish heading function
def stylish_heading():
    heading = figlet_format("Pixel Phantom X", font="doom", width=1000)
    print(colored(heading, "green"))

# ✅ Subtle adversarial noise (Inspired by Glaze)
def apply_disruptive_noise(image, noise_level="Min"):
    noise_intensity = 1 if noise_level == "Min" else 5  # Increased noise for Max
    noise = np.random.normal(0, noise_intensity, image.shape).astype(np.float32)
    return np.clip(image.astype(np.float32) + noise, 0, 255).astype(np.uint8)

# ✅ Subtle color-space manipulation (Inspired by Nightshade)
def apply_color_shift(image, noise_level="Min"):
    shift_value = 2 if noise_level == "Min" else 6  # Higher shift for Max
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    a = np.clip(a + np.random.randint(-shift_value, shift_value, a.shape), 0, 255)
    b = np.clip(b + np.random.randint(-shift_value, shift_value, b.shape), 0, 255)
    return cv2.cvtColor(cv2.merge([l, a.astype(np.uint8), b.astype(np.uint8)]), cv2.COLOR_LAB2BGR)

# ✅ Visible watermark for protection
def apply_visible_watermark(image, text="Protected"):
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    width, height = pil_image.size
    font = ImageFont.load_default()
    position = (width - 100, height - 30)
    draw.text(position, text, fill=(255, 255, 255))
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

# ✅ Invisible watermark (LSB Steganography, randomized pixels)
def apply_hidden_watermark(image, secret_message="Protected"):
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

# ✅ Edge distortion for AI disruption
def apply_edge_masking(image, noise_level="Min"):
    canny_min = 80 if noise_level == "Min" else 30
    canny_max = 120 if noise_level == "Min" else 180
    edges = cv2.Canny(image, canny_min, canny_max)
    blurred_edges = cv2.GaussianBlur(edges, (3, 3), 0)
    return cv2.addWeighted(image, 0.85, cv2.cvtColor(blurred_edges, cv2.COLOR_GRAY2BGR), 0.15, 0)

# ✅ Metadata poisoning function
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

    # Ensure image is in JPEG format for EXIF metadata
    img = Image.open(image_path)
    if img.format != "JPEG":
        image_path = image_path.rsplit(".", 1)[0] + ".jpg"
        img = img.convert("RGB")
        img.save(image_path, "jpeg")

    piexif.insert(exif_bytes, image_path)
    print(f"✅ Metadata poisoning applied: {image_path}")
