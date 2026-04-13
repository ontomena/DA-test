from PIL import Image

# Create placeholder images for sound posts
placeholders = {
    'geo-sound.jpg': '#3a6c8e',
    'barrow-sound.jpg': '#4a7c9e',
    'ambulant-sound.jpg': '#5a8c9e'
}

for filename, color in placeholders.items():
    img = Image.new('RGB', (600, 600), color)
    img.save(filename, 'JPEG')

print("Sound post placeholder images created")
