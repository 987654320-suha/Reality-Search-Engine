import easyocr
import cv2

reader = easyocr.Reader(['en'])

def extract_text(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return ""

    try:
        results = reader.readtext(image)

        text = " ".join(
            [item[1] for item in results]
        )

        return text

    except Exception as e:
        print("OCR Error:", e)
        return ""