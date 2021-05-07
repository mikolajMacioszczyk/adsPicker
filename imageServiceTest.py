import tempfile

from services.imageService import ImageService
import cv2


image = cv2.imread("D:\\test.png")
if image is not None:
    ims = ImageService()
    ims.saveImage("useCase.png", image)


