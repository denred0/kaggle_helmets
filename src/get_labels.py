import pandas as pd
import pickle
import cv2

from pathlib import Path

from tqdm import tqdm
from sklearn.preprocessing import LabelEncoder


def get_all_files_in_folder(folder, types):
    files_grabbed = []
    for t in types:
        files_grabbed.extend(folder.rglob(t))
    files_grabbed = sorted(files_grabbed, key=lambda x: x)
    return files_grabbed


data_all = pd.read_csv('data/train_labels.csv')
data = data_all[['video_frame', 'label', 'left', 'top', 'width', 'height']]

label_encoder = LabelEncoder()
labels = data['label'].tolist()
labels = list(dict.fromkeys(labels))

encoded = label_encoder.fit_transform(labels)

# save labels dict to file
with open('label_encoder.pkl', 'wb') as le_dump_file:
    pickle.dump(label_encoder, le_dump_file)

images = get_all_files_in_folder(Path('data/mp4_to_png/output'), ['*.png'])

for image in tqdm(images, total=len(images)):
    img = cv2.imread(str(image), cv2.IMREAD_COLOR)

    h, w = img.shape[:2]

    data_label = []

    data_image = data[data['video_frame'] == image.stem]

    for index, row in data_image.iterrows():
        # print(row[0])
        # if row[0] == image.stem:
        # label = row[1]
        label = label_encoder.classes_.tolist().index(row[1])
        xcenter = (int(row[2]) + int(row[4]) / 2) / w
        ycenter = (int(row[3]) + int(row[5]) / 2) / h
        w_norm = int(row[4]) / w
        h_norm = int(row[5]) / h
        if w_norm > 1:
            w_norm = 1
            print('w_norm > 1')
        if h_norm > 1:
            h_norm = 1
            print('h_norm > 1')
        if xcenter > 1:
            xcenter = 1
            print('xcenter > 1')
        if ycenter > 1:
            ycenter = 1
            print('ycenter > 1')
        if xcenter < 0:
            xcenter = 0
            print('xcenter < 0')
        if ycenter < 0:
            ycenter = 0
            print('ycenter < 0')
        data_label.append([label, xcenter, ycenter, w_norm, h_norm])

    with open('data/mp4_to_png/output/' + image.stem + '.txt', 'w') as f:
        for item in data_label:
            row = str(0) + ' ' + str(item[1]) + ' ' + str(item[2]) + ' ' + str(item[3]) + ' ' + str(item[4])
            f.write("%s\n" % row)

# print(data.head())
