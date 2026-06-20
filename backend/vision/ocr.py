import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image_path):
    results = reader.readtext(image_path)

    text = " ".join([item[1] for item in results])

    return text