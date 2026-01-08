#!/usr/bin/env python3
"""
C64 Charset to PNG Converter
Reads the C64 character set binary file and creates a PNG sprite sheet
with all 256 characters in a 16x16 grid (white background, black characters).
"""

from PIL import Image
import sys


def read_charset(filepath):
    """Read the C64 charset binary file."""
    with open(filepath, 'rb') as f:
        data = f.read()

    if len(data) != 2048:
        raise ValueError(f"Invalid charset file size: {len(data)} bytes (expected 2048)")

    return data


def create_charset_png(charset_data, output_path):
    """
    Create a PNG sprite sheet from charset data.

    Args:
        charset_data: 2048 bytes of charset data (256 chars × 8 bytes)
        output_path: Path to save the PNG file
    """
    # Create 128x128 image (16 chars × 8 pixels in each dimension)
    width = 16 * 8  # 128 pixels
    height = 16 * 8  # 128 pixels

    # Create image with white background
    img = Image.new('RGB', (width, height), color='white')
    pixels = img.load()

    # Process all 256 characters
    for char_index in range(256):
        char_offset = char_index * 8  # Each character is 8 bytes

        # Calculate position in 16x16 grid
        grid_x = char_index % 16
        grid_y = char_index // 16
        offset_x = grid_x * 8
        offset_y = grid_y * 8

        # Draw each pixel of the 8x8 character
        for y in range(8):
            byte = charset_data[char_offset + y]
            for x in range(8):
                # Check if bit is set (bit 7 is leftmost pixel)
                if byte & (1 << (7 - x)):
                    # Set pixel to black
                    pixels[offset_x + x, offset_y + y] = (0, 0, 0)

    # Save the image
    img.save(output_path)
    print(f"Charset PNG saved to: {output_path}")


def main():
    """Main entry point."""
    input_file = 'c64-charset.bin'
    output_file = 'c64-charset.png'

    # Allow command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    try:
        print(f"Reading charset from: {input_file}")
        charset_data = read_charset(input_file)

        print(f"Creating PNG sprite sheet...")
        create_charset_png(charset_data, output_file)

        print(f"Success! Image is 128x128 pixels (16×16 grid of 8×8 characters)")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
