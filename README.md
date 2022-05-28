# OCRad
A quick and easy way to recognize the text in your clipboard! Just take a screenshot of any text, run `OCRad.py`, and the text will be recognized and copied to your clipboard.
I use this just about everyday, seriously. I have a shortcut to the script on my desktop, which I can just click on to run. Super convenient. On my old Macbook, I had a shortcut to it on my touchbar (you need to use automator to make that happen I think).

## Getting Started
First install the requirements with `pip install -r requirements.txt`

Now, this uses the Google Vision API. So grab yourself your very own `ServiceAccountToken.json` (find some instructions [here](https://cloud.google.com/vision/docs/ocr)). And you're good to go, just run `OCRad.py`!

The script will save your last image to the directory the script is in, so that you can still access your screenshot if you didnt want to actually convert it to text.

 
 Note: I don't think `OCRadApp.py` works, that was just a test on Mac that I abandoned, but if anyone wants to give it a soht and fix it, please be my guest haha!
