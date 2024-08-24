# Image Encryption Tool

**Image Encryption Tool** is a simple Python application that allows you to encrypt and decrypt images using basic pixel manipulation techniques. This tool performs encryption by adding a key value to each pixel and decryption by subtracting the same key value.

## Features

- **Encrypt Images**: Modify pixel values by adding a key value.
- **Decrypt Images**: Restore original images by subtracting the key value.
- **Simple Mathematical Operations**: Basic operations to ensure pixel values remain within valid range.

## Installation

Ensure you have Python installed, then install the required libraries using pip:

```bash
pip install pillow numpy
```

## Usage

1. **Clone the Repository**

    ```bash
    git clone https://github.com/DevRaas/ImageEncryptionTool.git
    cd ImageEncryptionTool
    ```

2. **Run the Script**

    ```bash
    python image_encryption_tool.py
    ```

3. **Follow the Prompts**

    - Choose to encrypt or decrypt an image.
    - Provide the path to the image file.
    - Enter a key value (integer) used for encryption and decryption.
    - Specify the path where the output image should be saved.

### Example

#### Encrypting an Image

```
Choose an option (1/2): 1
Enter the path to the image: example.jpg
Enter the key value (integer): 50
Enter the path to save the encrypted image: encrypted_example.jpg
```

#### Decrypting an Image

```
Choose an option (1/2): 2
Enter the path to the image: encrypted_example.jpg
Enter the key value (integer): 50
Enter the path to save the decrypted image: decrypted_example.jpg
```

## Code Overview

- **`encrypt_image(image_path, key, output_path)`**: Encrypts an image by adding a key value to each pixel.
- **`decrypt_image(image_path, key, output_path)`**: Decrypts an image by subtracting a key value from each pixel.
- **`main()`**: Provides a command-line interface to interact with the tool.

## Contributing

Contributions are welcome! Feel free to fork the repository, make your changes, and create a pull request. You can also open issues for bugs or feature requests.


## Contact

For questions or feedback, please contact [roshanajith7911@gmail.com].

## Acknowledgements

- Thanks to the Pillow and NumPy libraries for making image processing and array handling straightforward.

