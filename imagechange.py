import cv2
import os

if __name__ == '__main__':
        def imagechange():
        names = os.listdir('./pokemon/')
        names.sort()
	os.makedirs(save_path,exist_ok=True)
        for name in names:
            os.makedirs(save_path,exist_ok=True)
            img = cv2.imread('./pokemon/' + name)
            width, height = 64, 64
            img = cv2.resize(img, (width, height))
            cv2.imwrite('./pokemon64/' + name, img)
