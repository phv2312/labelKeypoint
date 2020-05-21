import cv2
import json
import os

import matplotlib.pyplot as plt
PATH_DATA = "../../data/processed_hor01"
def imgshow(im):
    plt.imshow(im)
    plt.show()

def save_visualize_single(json_data, cv2_image, vis_folder, img_name):
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
        cv2.putText(cv2_image, label, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), thickness=1)

    # imgshow(cv2.cvtColor(cv2_image, cv2.COLOR_RGB2BGR))
    vis_file = os.path.join(vis_folder, image_name)
    cv2.imwrite(vis_file, cv2_image)

def check_valid_folder(folder_name):
    '''
        A valid folder must comprise two necessary sub folder for visualizing (images, labels)
    '''
    image_folder = os.path.join(folder_name, "images")

    label_folder = os.path.join(folder_name, "labels")


    results = True
    results = results and os.path.isdir(image_folder)
    results = results and os.path.isdir(label_folder)

    return results

if __name__ == '__main__':
    # json_fn = "/home/kan/Desktop/Cinnamon/pose/labelKeypoint/scripts/processed_hor01/1/labels/hor01_101_104_106_108_k_B_POSE_B0003.json"
    # imag_fn = "/home/kan/Desktop/Cinnamon/pose/labelKeypoint/scripts/processed_hor01/1/images/hor01_101_104_106_108_k_B_POSE_B0003.png"

    for id_folder in os.listdir(PATH_DATA):
        processed_folder = os.path.join(PATH_DATA, id_folder)

        if check_valid_folder(processed_folder):
            print("On visualizing folder id", id_folder)
            image_folder = os.path.join(processed_folder, "images")
            label_folder = os.path.join(processed_folder, "labels")
            vis_folder = os.path.join(processed_folder, "vis_resutls")
            if os.path.isdir(vis_folder) is False:
                os.makedirs(vis_folder)

            # process each image
            for image_name in os.listdir(image_folder):

                full_img_path = os.path.join(image_folder, image_name)
                full_label_path = os.path.join(label_folder, os.path.splitext(image_name)[0]+".json")

                if os.path.isfile(full_label_path):#exist json label file of image_name
                    with open(full_label_path, 'r') as json_file:
                        json_data = json.load(json_file)

                    image_data = cv2.imread(full_img_path)

                    save_visualize_single(json_data, image_data, vis_folder, image_name)



    # json_data = json.load(open(json_fn, 'r'))
    # imag_data = cv2.imread(imag_fn)

    # visualize_single(json_data, imag_data)