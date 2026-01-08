# 8-bit Font Converter

A Python tool to convert the Commodore 64 character set (and other 8-bit fonts) into PNG sprite sheets for use in web applications.

## Features

- Converts binary charset files to PNG sprite sheets
- Outputs a 128×128 pixel image containing all 256 characters in a 16×16 grid
- Each character is 8×8 pixels

![C64 Charset](./c64-charset.png)

## Requirements

- Python 3.7 or higher
- Pillow (PIL)

## Installation

1. Clone this repository or download the files

2. Install virtual environment and dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or with a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### Basic Usage

Convert the C64 charset to PNG:
```bash
python3 charset_to_png.py
```

This will read `c64-charset.bin` and create `c64-charset.png`.

### Custom Input/Output

Specify custom input and output files:
```bash
python3 charset_to_png.py input.bin output.png
```

### Using the Generated PNG

The generated PNG is a sprite sheet with all 256 characters arranged in a 16×16 grid. Each character is 8×8 pixels.

