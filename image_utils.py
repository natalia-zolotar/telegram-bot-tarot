from PIL import Image

def generate_cards_image(card_names, theme, output='result.jpg'):
    images = [
        Image.open(f'src/{theme}/{card}.webp')
        for card in card_names
    ]

    width, height = images[0].size

    result = Image.new("RGB", (width * len(images), height))

    x = 0
    for img in images:
        result.paste(img, (x, 0))
        x += width

    result.save(output)

    return output