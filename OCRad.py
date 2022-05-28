# -*- coding: utf-8 -*-

import os, io
from google.cloud import vision
from PIL import ImageGrab
import pyperclip

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    fullText=texts[0].description


    pyperclip.copy(fullText)


    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "ServiceAccountToken.json"

im = ImageGrab.grabclipboard()

im.save('lastOCRImage.png','PNG')

detect_text("lastOCRImage.png")
