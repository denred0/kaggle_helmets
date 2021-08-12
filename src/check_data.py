import pickle
from pathlib import Path

def get_all_files_in_folder(folder, types):
    files_grabbed = []
    for t in types:
        files_grabbed.extend(folder.rglob(t))
    files_grabbed = sorted(files_grabbed, key=lambda x: x)
    return files_grabbed

images = get_all_files_in_folder(Path('data/mp4_to_png/output'), ['*.png'])
txts = get_all_files_in_folder(Path('data/mp4_to_png/output'), ['*.txt'])

print(len(images))
print(len(txts))

label_encoder = pickle.load(open("label_encoder.pkl", 'rb'))
print(label_encoder.classes_)
print(len(label_encoder.classes_))
