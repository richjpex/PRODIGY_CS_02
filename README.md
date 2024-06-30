# PRODIGY_CS_02
A simple image encryption tool using pixel manipulation
## Task
Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.
## Pixel Manipulation Algorithm
The algorithm first swaps the red and blue channels, and then swaps the blue and green channels during encryption. For decryption, it reverses the operations by swapping the blue and green channels back, and then swapping the red and blue channels back.

## Usage

Install dependencies

`pip install requirements.txt`


Run the program

To encrypt image:

`python main.py --encrypt image.jpg`

To decrypt image:

`python main.py --decrypt image.jpg`
