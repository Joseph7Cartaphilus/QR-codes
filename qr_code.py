import qrcode


def get_qrcode(url='https://gogle.com', name='default'):
    """Вводим URL и создаем на основе него qr code с названием"""
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created open with {name}.png'


def main():
    print(get_qrcode(url='write-your-url-here', name='write-qr_code-name'))


if __name__ == '__main__':
    main()
