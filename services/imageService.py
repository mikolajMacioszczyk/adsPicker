import tempfile
from pathlib import Path
import cv2


class ImageService:
    def __init__(self):
        self.dir = tempfile.gettempdir()+"\\adsPicker"
        Path(self.dir).mkdir(parents=True, exist_ok=True)

    def saveImage(self, path, image):
        cv2.imwrite(f"{self.dir}\\{path}", image)

    def getImage(self, path):
        return cv2.imread(f"{self.dir}\\{path}")
