from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Simple encryption: Add key value to each pixel
    encrypted_pixels = (pixels + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))

    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Simple decryption: Subtract key value from each pixel
    decrypted_pixels = (pixels - key) % 256
    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))

    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    
    choice = input("Choose an option (1/2): ")
    if choice not in ['1', '2']:
        print("Invalid choice. Please select either 1 or 2.")
        return

    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the key value (integer): "))

    if choice == '1':
        output_path = input("Enter the path to save the encrypted image: ")
        encrypt_image(image_path, key, output_path)
    elif choice == '2':
        output_path = input("Enter the path to save the decrypted image: ")
        decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()
