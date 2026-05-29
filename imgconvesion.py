import os
from PIL import Image

FOLDER_PATH = r"D:\Abdullah\TN"

# Find the files
files = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith('.tn3')]
print(f"Found {len(files)} files to convert...")

for file in files:
    full_old_path = os.path.join(FOLDER_PATH, file)

    new_filename = os.path.splitext(file)[0].strip() + '.jpg'
    full_new_path = os.path.join(FOLDER_PATH, new_filename)
    
    try:
        with Image.open(full_old_path) as img:
            img.convert('RGB').save(full_new_path, 'JPEG')
        print(f"Successfully converted: {file}")
    except Exception as e:
        print(f"Could not convert {file}. Error: {e}")

print("All done!")