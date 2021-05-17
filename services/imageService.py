import tempfile
from pathlib import Path
import cv2
import os
import string
import random
from flask import send_from_directory


class ImageService:
    def __init__(self):
        self.dir = tempfile.gettempdir()+"\\adsPicker\\"
        Path(self.dir).mkdir(parents=True, exist_ok=True)

    def saveImage(self, path, image):
        cv2.imwrite(f"{self.dir}{path}", image)

    def saveFileStorage(self, image):
        path = f"{image.filename}"
        while os.path.isfile(f"{self.dir}{path}"):
            path = path + random.choice(string.ascii_letters)
        image.save(f"{self.dir}{path}")
        return path

    def downloadToFlask(self, fileName):
        try:
            return send_from_directory(self.dir, fileName, as_attachment=True)
        except FileNotFoundError:
            return None

    def getImage(self, path):
        return cv2.imread(f"{self.dir}{path}")
