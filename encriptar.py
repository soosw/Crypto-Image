from PIL import Image
import io

try:
    # to handle the path with escape characters
    path = input(r'Enter path of Image : ')

    # taking encryption key as input
    key = int(input('Enter Key for encryption of Image (just numbers) : '))

    # print path of image file and encryption key that
    # we are using
    print('The path of file : ', path)
    print('Key for encryption : ', key)

    # open image using PIL
    with Image.open(path) as img:
        # convert image to byte array
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format=img.format)
        image = bytearray(img_byte_array.getvalue())

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # open image for writing purpose
        with open(path, 'wb') as fin:
            # writing encrypted data in image
            fin.write(image)

        print('Encryption Done...')

except FileNotFoundError:
    print(f'Error: File not found at path {path}')
except PermissionError:
    print(f'Error: Permission denied for file at path {path}')
except Exception as e:
    print(f'Error caught: {e.__class__.__name__} - {e}')
