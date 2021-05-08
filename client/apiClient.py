import requests
import cv2
import numpy as np
import base64

if __name__ == '__main__':
    adId = None
    while not adId.isdigit():
        print("Type id: ")
        adId = input()
    url = f"http://127.0.0.1:5000/api/image/byId?id={adId}"
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)

        imageString = base64.b64decode(response.text)

        #  convert binary data to numpy array
        nparr = np.fromstring(imageString, np.uint8)

        #  let opencv decode image to correct format
        img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed! Status code: ", response.status_code)
