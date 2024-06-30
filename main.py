import argparse
from PIL import Image
import os

def get_output_path(input_path, new_name):
    directory, _ = os.path.split(input_path)
    _, ext = os.path.splitext(input_path)
    return os.path.join(directory, f"{new_name}{ext}")

def encrypt(image_path):
    """
    Encrypt an image by swapping red, green, and blue channels.
    """
    image = Image.open(image_path)
    pixels = image.load()
    
    for i in range(image.size[0]):  # width of the image
        for j in range(image.size[1]):  # height of the image
            r, g, b = pixels[i, j]
            # Swap red and blue channels
            r, g, b = b, g, r
            # Swap blue and green channels
            r, g, b = r, b, g
            pixels[i, j] = (r, g, b)
    
    encrypted_path = get_output_path(image_path, 'encrypted')
    image.save(encrypted_path)
    print(f"Image encrypted and saved as {encrypted_path}")

def decrypt(image_path):
    """
    Decrypt an image by swapping red, green, and blue channels in reverse order.
    """
    image = Image.open(image_path)
    pixels = image.load()
    
    for i in range(image.size[0]):  # width
        for j in range(image.size[1]):  # height
            r, g, b = pixels[i, j]
            # Reverse swap blue and green channels
            r, g, b = r, b, g
            # Reverse swap red and blue channels
            r, g, b = b, g, r
            pixels[i, j] = (r, g, b)
    
    decrypted_path = get_output_path(image_path, 'decrypted')
    image.save(decrypted_path)
    print(f"Image decrypted and saved as {decrypted_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt an image by swapping red, green, and blue channels")
    parser.add_argument('--encrypt', type=str, help='Path to the image to encrypt')
    parser.add_argument('--decrypt', type=str, help='Path to the image to decrypt')
    
    args = parser.parse_args()
    
    if args.encrypt:
        encrypt(args.encrypt)
    elif args.decrypt:
        decrypt(args.decrypt)
    else:
        print("Please provide either --encrypt or --decrypt followed by the image path.")
