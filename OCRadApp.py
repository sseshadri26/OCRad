# -*- coding: utf-8 -*-

# used to make a application bar at the top of the screen for macOS. I made a seperate Automator script to make running this conventient on macOS but I don't have it on this laptop. I'm not even sure if this script works on macOS...the perils of switching to Windows before testing this on mac!
import rumps
from google.cloud import vision
import io
import objc


class OCRadApp(object):
    def __init__(self):
        self.config = {
            "app_name": "OCRad",
            "start": "Convert Clipboard Image",
        }
        self.app = rumps.App(self.config["app_name"])

        self.set_up_menu()
        self.start_button = rumps.MenuItem(title=self.config["start"], callback=self.detect_text)
        self.app.menu = [self.start_button]

    def set_up_menu(self):

        self.app.title = "📝"


    def run(self):
        self.app.run()

    def detect_text(self, sender):
        print("Running")
        #finds token from path
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "My\ Best\ Projects/OCRad/ServiceAccountToken.json"

        im = ImageGrab.grabclipboard()

        im.save('lastOCRImage.png','PNG')

        path = "lastOCRImage.png"


        #Detects text in the file.

        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')
        fullText=texts[0].description
        for text in texts:
            print('\n"{}"'.format(text.description))

        pyperclip.copy(fullText)


        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))




if __name__ == '__main__':
    app = OCRadApp()
    app.run()
