from PIL import Image, ImageDraw, ImageFont

# Create simple placeholder images with different colors
placeholders = {
    'geoambo.jpg': '#4a7c9e',
    'tabularasa.jpg': '#6b8e9e',
    'suitesix.jpg': '#5a8595',
    'cause.jpg': '#4a7c9e',
    'borderguide.jpg': '#6a8d9d',
    'lieofland.jpg': '#5b869c',
    'twotrees.jpg': '#4f8199',
    'workington.jpg': '#5d879a',
    'archive.jpg': '#687f8f'
}

for filename, color in placeholders.items():
    img = Image.new('RGB', (600, 600), color)
    img.save(filename, 'JPEG')

print("Placeholder images created")
