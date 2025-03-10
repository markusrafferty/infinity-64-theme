import os
import re

def blend_color(foreground, background="#000000"):
    """Blend a semi-transparent foreground color onto a background color."""
    
    fg_r = int(foreground[1:3], 16)
    fg_g = int(foreground[3:5], 16)
    fg_b = int(foreground[5:7], 16)
    alpha = int(foreground[7:9], 16) / 255.0
    
    bg_r = int(background[1:3], 16)
    bg_g = int(background[3:5], 16)
    bg_b = int(background[5:7], 16)
    
    new_r = round(fg_r * alpha + bg_r * (1 - alpha))
    new_g = round(fg_g * alpha + bg_g * (1 - alpha))
    new_b = round(fg_b * alpha + bg_b * (1 - alpha))
    
    return f"#{new_r:02X}{new_g:02X}{new_b:02X}"

def process_file(filepath):
    """Process a single JSON file and replace transparent foreground colors."""

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        
    background = re.search(r'\"editor\.background\": \"(#[0-9A-Fa-f]{6})\"', content).group(1)

    count = 0
    def replace_color(match):
        nonlocal count
        full_match = match.group(0)
        color = match.group(2)
        
        if len(color) == 9:  # Check if the color has an alpha channel
            blended = blend_color(color, background)
            count += 1
            return full_match.replace(color, blended)
        return full_match
    
    new_content = re.sub(r'(\"foreground\": \")(#[0-9A-Fa-f]{8})\"', replace_color, content)
    
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(new_content)
    
    print(f"Processed: {filepath} - Replacements: {count}")

def process_directory(directory):
    """Process all JSON files in the given directory."""

    json_files = [f for f in os.listdir(directory) if f.endswith(".json")]
    print(f"Found {len(json_files)} JSON files.")
    
    for filename in json_files:
        process_file(os.path.join(directory, filename))

if __name__ == "__main__":
    process_directory("themes/")
