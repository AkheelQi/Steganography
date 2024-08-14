from PIL import Image

def encode_message(image_path, message, output_path):
    # Open the image
    image = Image.open('C:\\Users\\Muhammed Akheel\\OneDrive\\Desktop\\Posts\\input_image.png')
    encoded_image = image.copy()
    width, height = image.size
    message += chr(0)  # Add a null character to mark the end of the message
    message_bits = ''.join([format(ord(char), '08b') for char in message])

    # Encode the message bits into the image
    index = 0
    for y in range(height):
        for x in range(width):
            if index < len(message_bits):
                pixel = list(image.getpixel((x, y)))
                for n in range(3):  # Modify the RGB values
                    if index < len(message_bits):
                        pixel[n] = pixel[n] & ~1 | int(message_bits[index])
                        index += 1
                encoded_image.putpixel((x, y), tuple(pixel))
            else:
                break

    # Save the encoded image
    encoded_image.save(output_path)

# Example usage
encode_message('input_image.png', 'Hey! This is a secret message', 'encoded_image.png')

