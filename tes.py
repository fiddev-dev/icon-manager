import os
import json

# Ambil semua file .svg di folder saat ini
icons = [
    f[:-4] for f in os.listdir(".")
    if f.lower().endswith(".svg")
]

# Simpan ke ../icons.json
output_path = os.path.join("..", "icons.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(icons, f)

print(f"Generated {output_path} with {len(icons)} icons.")
