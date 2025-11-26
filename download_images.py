#!/usr/bin/env python3
"""
Simple Image Downloader for Date Ranker
This script helps you download images for your date locations.
"""

import urllib.request
import os

# Image URLs - UPDATE THESE with actual image URLs you find
IMAGES = {
    # Add your image URLs here
    # Format: 'date-id': 'image-url'

    # Example (replace with actual URLs):
    # 'vizcaya': 'https://example.com/vizcaya-image.jpg',
    # 'butterfly': 'https://example.com/butterfly-world.jpg',
}

def download_images():
    """Download images to the images folder"""

    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)

    for date_id, url in IMAGES.items():
        try:
            print(f"Downloading {date_id}...")

            # Determine file extension from URL
            ext = url.split('.')[-1].split('?')[0]
            if ext not in ['jpg', 'jpeg', 'png', 'webp']:
                ext = 'jpg'

            filename = f"images/{date_id}.{ext}"

            # Download the image
            urllib.request.urlretrieve(url, filename)
            print(f"✓ Saved: {filename}")

        except Exception as e:
            print(f"✗ Failed to download {date_id}: {e}")

    print("\nDone! Check the 'images' folder.")
    print("Now update index.html to use: img: 'images/{id}.jpg'")

if __name__ == "__main__":
    if not IMAGES:
        print("No images configured!")
        print("\nHow to use this script:")
        print("1. Find images online (Google Images, venue websites, etc.)")
        print("2. Right-click → 'Copy image address'")
        print("3. Add to the IMAGES dictionary in this file")
        print("4. Run: python download_images.py")
    else:
        download_images()
