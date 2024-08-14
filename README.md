# Stenography

Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. In contrast with this in Cryptograpy a file, message, image, or video is keyed transformed in order to hide information. Steganography requires a carrier/payload in order to carry Obfuscated information.

This code demonstrates a simple method of steganography to hide a secret message within an image. It uses the Pillow library to manipulate image pixels.

Encoding Function:
encode_message(image_path, message, output_path):
-Opens the input image.
-Converts the message into binary format.
-Encodes the message bits into the least significant bits of the image’s pixel values.
-Saves the modified image with the hidden message.

Decoding Function:
-decode_message(image_path):
-Opens the encoded image.
-Extracts the message bits from the least significant bits of the pixel values.
-Converts the bits back into characters to reveal the hidden message.
