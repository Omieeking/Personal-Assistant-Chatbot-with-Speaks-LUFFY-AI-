import ctypes
import os
import glob
import random
import time

# SPI_SETDESKWALLPAPER constant value
SPI_SETDESKWALLPAPER = 20

def set_wallpaper(image_path):
    # Check if the file exists
    if not os.path.exists(image_path):
        return False, f"Error: File not found - {image_path}"

    # Update the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    return True, f"Wallpaper changed to: {image_path}"

def rotate_wallpapers(directory):
    # Get a list of image files in the specified directory
    image_files = glob.glob(os.path.join(directory, '*.jpg')) + glob.glob(os.path.join(directory, '*.png'))

    if not image_files:
        return False, f"No image files found in {directory}"

    # Shuffle the list of image files
    random.shuffle(image_files)

    # Set each wallpaper only once
    for image_path in image_files:
        success, message = set_wallpaper(image_path)
        if success:
            return success, message

    return False, "No valid wallpapers found"