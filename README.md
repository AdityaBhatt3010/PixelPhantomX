# PixelPhantomX

PixelPhantomX is a powerful image obfuscation tool designed to generate ghost images that confuse AI models. In an era where generative AI scrapes and repurposes artwork without the consent of creators, this tool acts as a defensive mechanism. By applying various adversarial techniques, such as noise injection, color-space manipulation, edge distortion, and watermarking, PixelPhantomX helps protect digital images from unauthorized AI training and exploitation.

![Image](https://github.com/user-attachments/assets/ab9d13cb-9fa0-400d-8a8b-e75fb312b70c) <br/>

## Features

- **Adversarial Noise Injection** (Inspired by Glaze & Nightshade)
- **Customizable Noise Levels** (Min/Max)
- **Watermarking** (Visible & Invisible Steganographic Protection)
- **Edge Distortion** for AI Confusion
- **Metadata Poisoning** to mislead AI training
- **Command-line Interface** for easy use

## Installation

Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Run the tool via the command line:

```sh
python PixelPhantomX.py -iP input_image_path -n noise -oP output_image_path -w watermark_text
```

### Parameters:

| Parameter | Description                                  |
| --------- | -------------------------------------------- |
| `-iP`     | Path to the input image (with extension)     |
| `-n`      | Noise level (`Min` or `Max`)                 |
| `-oP`     | Output image path (without extension)        |
| `-w`      | Custom watermark text (default: `Protected`) |

### Example:

```sh
python PixelPhantomX.py -iP sample.jpg -n Max -oP output_image -w Confidential
```

### Help Menu

To view available commands, run:

```sh
python PixelPhantomX.py -h
```

## License

This project is licensed under the MIT License.

## Author

**Aditya Bhatt**\

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

### Disclaimer:

This tool is intended for **ethical** use only. The author is not responsible for any misuse of this software.

