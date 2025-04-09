# PixelPhantomX: Ghost images to confuse AI models

PixelPhantomX is a powerful image obfuscation tool designed to generate ghost images that confuse AI models. In an era where generative AI scrapes and repurposes artwork without the consent of creators, this tool acts as a defensive mechanism. By applying various adversarial techniques, such as noise injection, color-space manipulation, edge distortion, and watermarking, PixelPhantomX helps protect digital images from unauthorized AI training and exploitation.

![Image](https://github.com/user-attachments/assets/d94c29e8-b2ca-40c6-92d7-fc1b51f745a1) <br/>

## Features

- **Adversarial Noise Injection** (Inspired by Glaze & Nightshade)
- **Customizable Noise Levels** (Min/Max)
- **Watermarking** (Visible & Invisible Steganographic Protection)
- **Edge Distortion** for AI Confusion
- **Metadata Poisoning** to mislead AI training
- **Command-line Interface** for easy use

## Installation

Direct Install from PyPI

```sh
pip install PixelPhantomX
```

Alternatively, install via setup.py:

```sh
python setup.py install
```

Otherwise, install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Run the tool via the command line:

```sh
python PixelPhantomX.py -iP input_image_path -n noise -oP output_image_path -w watermark_text
```

## Repository Structure

```
PixelPhantomX/
├── PixelPhantomX.py               # Main script: runs full image protection pipeline
├── PixelPhantomX_Minimal.py      # Lightweight version with core functionality
├── Img_Poision.py                # Core image poisoning logic
├── RP_Struct.py                  # Runtime parameter or response structure definitions
├── utilities.py                  # Utility functions for adversarial techniques
│
├── README.md                     # Project overview and usage instructions
├── Requirements.txt              # Python dependencies
├── setup.py                      # Setup script for installation
├── pyproject.toml                # Project metadata for build tools
│
├── LICENSE                       # License information
├── .gitignore                    # Git ignored files
├── .gitattributes                # Git settings (e.g. end-of-line normalization)
│
├── /images/                      # Example input/output images and UI assets
│   ├── Input.png
│   ├── Output.jpg
│   ├── PixelPhantomX_Run.png
│   └── Help.png
│
└── .github/
    └── workflows/
        └── python-app.yml        # GitHub Actions workflow for linting and testing
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
python PixelPhantomX.py -iP Input.png -oP Output -n Min -w AdityaBhatt3010
```

### Help Menu

To view available commands, run:

```sh
python PixelPhantomX.py -h
```

### Alternative Usage - Interactive Mode

For a guided, interactive experience instead of command-line arguments, use:

```sh
python PixelPhantomX_Minimal.py
```

## Screenshots

- **Help Prompt Screenshot**
  ```sh
  python PixelPhantomX.py -h
  ```
  ![Image](https://github.com/user-attachments/assets/8548e5ff-8d03-4668-adfe-694826f4420f) <br/>


- **Run Code Example:**
  ```sh
  python PixelPhantomX.py -iP Input.png -oP Output -n Min -w AdityaBhatt3010
  ```
  ![Image](https://github.com/user-attachments/assets/5e2be7b1-f71a-4dbc-bab0-cc435611deb9) <br/>


- **Input Image Screenshot**
  <br/> ![Image](https://github.com/user-attachments/assets/f553dd8a-33dc-4db4-a4bb-f61362a6adb9) <br/>

- **Output Image Screenshot**
  <br/> ![Image](https://github.com/user-attachments/assets/98a3ee41-467d-41cf-998b-a58d50396a31) <br/>

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

### Disclaimer:
This tool is intended for **ethical** use only. The author is not responsible for any misuse of this software.

