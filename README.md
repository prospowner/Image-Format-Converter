# Batch Image Converter

An automated backend file utility written in Python that leverages the Pillow library to safely batch-process, convert, and transcode proprietary or raw image files (like `.tn3`) into widely compatible `.jpg` images.

## Features
* **Dynamic Relative Storage Paths:** Bypasses hardcoded drive directories. The script automatically determines its own host environment context layout using `os.path.abspath(__file__)`, making it completely universal and secure across different machines.
* **Automated Environment Provisioning:** Includes built-in directory integrity checks. If the necessary operational storage folder does not exist at launch, the script automatically provisions a localized `/images` folder on the fly.
* **Safe Binary Transcoding:** Employs Pillow's memory-safe context managers (`with Image.open()`) to safely parse binary streams, transcode pixels to the standard `RGB` color space, and encode them into optimized JPEGs.
* **Error-Resilient Execution Loops:** Implemented with strict `try/except` protective handling blocks, ensuring that a single corrupted or malformed source file will not crash or interrupt the broader automation process.

## Dependencies
This utility requires the Python Imaging Library (Pillow) to process image structures. 
You can install it seamlessly via pip:
```bash
pip install Pillow
