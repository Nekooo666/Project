import cv2
from numba import jit
import numpy as np

class webcam:

    def ascii():
        cam = cv2.VideoCapture(0)


        @jit(nopython=True)
        def to_ascii_art(frame, images, box_height=12, box_width=16):
            height, width = frame.shape
            for i in range(0, height, box_height):
                for j in range(0, width, box_width):
                    roi = frame[i:i + box_height, j:j + box_width]
                    best_match = np.inf
                    best_match_index = 0
                    for k in range(1, images.shape[0]):
                        total_sum = np.sum(np.absolute(np.subtract(roi, images[k])))
                        if total_sum < best_match:
                            best_match = total_sum
                            best_match_index = k
                    roi[:,:] = images[best_match_index]
            return frame


        def generate_ascii_letters():
            images = []
            #letters = "# $%&\\'()*+,-./0123456789:;<=>?@[]^_`{|}~"
            letters = "#&\\'(),-./0123456789:;[]_`{|}~"
            for letter in letters:
                img = np.zeros((12, 16), np.uint8)
                img = cv2.putText(img, letter, (0, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 255)
                images.append(img)
            return np.stack(images)


        images = generate_ascii_letters()


        print("goo")
        while True:
            ret, frame = cam.read()


            if ret == True:
                frame = cv2.flip(frame, 1)
                gb = cv2.GaussianBlur(frame, (5, 5), 0)
                can = cv2.Canny(gb, 127, 31)
                ascii_art = to_ascii_art(can, images)
                cv2.imshow('ASCII ART', ascii_art)


                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        print("stop")


        cam.release()
        cv2.destroyAllWindows()