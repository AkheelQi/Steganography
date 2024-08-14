from PIL import Image

def decode_message(image_path):
    # Open the image
    image = Image.open('C:\\Users\\Muhammed Akheel\\OneDrive\\Desktop\\Posts\\encoded_image.png')
    width, height = image.size
    message_bits = []

    # Extract the message bits from the image
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            for n in range(3):  # Extract from RGB values
                message_bits.append(pixel[n] & 1)

    # Convert bits to characters
    message = ''.join(chr(int(''.join(map(str, message_bits[i:i+8])), 2)) for i in range(0, len(message_bits), 8))
    return message.split(chr(0))[0]  # Remove the null character

# Example usage
hidden_message = decode_message('encoded_image.png')
print(f'Decoded message: {hidden_message}')
