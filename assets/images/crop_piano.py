from PIL import Image

# Create a representative piano key strip image (since we can't download)
# This will be a placeholder - Simon will replace with actual cropped logo2.jpg
img = Image.new('RGB', (1200, 80), '#2a2a2a')  # Dark piano key color
img.save('piano-strip.jpg', 'JPEG')
print("Piano strip placeholder created")
