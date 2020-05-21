import cv2
import json

import matplotlib.pyplot as plt
def imgshow(im):
    plt.imshow(im)
    plt.show()

def visualize_single(json_data, cv2_image):
    kps = json_data['shapes']
    bbox = json_data['bounding_box']

    # draw bounding boxes
    x, y, w, h = bbox['x'], bbox['y'], bbox['w'], bbox['h']
    x = int(x)
    y = int(y)
    w = int(w)
    h = int(h)

    cv2.rectangle(cv2_image, (x,y), (x + w, y + h), (255,0,0), 5)

    # draw key points
    for kp_dct in kps:
        point = kp_dct['points']
        label = kp_dct['label']

        x, y = point[0]
        x = int(x)
        y = int(y)

        cv2.circle(cv2_image, (x, y), 10, (0,255,0), thickness=5)
        cv2.putText(cv2_image, label, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255,0,0), thickness=1)

    imgshow(cv2.cvtColor(cv2_image, cv2.COLOR_RGB2BGR))


if __name__ == '__main__':
    json_fn = "/home/kan/Desktop/Cinnamon/pose/labelKeypoint/scripts/processed_hor01/1/labels/hor01_101_104_106_108_k_B_POSE_B0003.json"
    imag_fn = "/home/kan/Desktop/Cinnamon/pose/labelKeypoint/scripts/processed_hor01/1/images/hor01_101_104_106_108_k_B_POSE_B0003.png"

    json_data = json.load(open(json_fn, 'r'))
    imag_data = cv2.imread(imag_fn)

    visualize_single(json_data, imag_data)