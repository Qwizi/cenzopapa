from PIL import Image, ImageDraw, ImageFilter


class WatermarkService:
    logo_path: str

    def __init__(self):
        self.logo_path = "app/logo.png"

    def add_watermark(self, path):
        logo = Image.open(self.logo_path)
        image_to_process = Image.open(path)
        image_copy = image_to_process.copy()
        position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
        image_copy.paste(logo, position, logo)
        image_copy.save(path)