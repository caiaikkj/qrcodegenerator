import qrcode

def generate_qr_code (text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#293241")
    img.save(file_name)

# Digite o texto que estará contido no QR code
text = "https://www.youtube.com/watch?v=rY-FJvRqK0E"
# Dê um nome para salvar o arquivo
file_name = "flamingo.png"
# Gerar o QR code
generate_qr_code(text, file_name)
print(f"QR code saved as {file_name}")