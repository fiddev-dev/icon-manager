import os
import json

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

# List all .svg files in the current directory
svg_files = [f for f in os.listdir(script_dir) if f.endswith('.svg')]

# Extract names without .svg extension
icon_names = [os.path.splitext(f)[0] for f in svg_files]

# Write to ../icons.json
output_path = os.path.join(parent_dir, 'icons.json')
with open(output_path, 'w') as f:
    json.dump(icon_names, f)