import base64
from io import BytesIO

from html2image import Html2Image
from PIL import Image

hti = Html2Image(browser_executable="/usr/bin/chromium")

def execute(size: int, pl: str):
    hti.screenshot(
        size=(size, size),
        url=f"http://davioitu.pythonanywhere.com/playlistprint?playlistURI={pl}",
        save_as="scr.png",
    )

    image = Image.open("scr.png")
    image = image.convert("RGB")
    image = image.resize((700, 700), Image.Resampling.HAMMING)

    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())

    return img_str
