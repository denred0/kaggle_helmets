# from __future__ import print_function, division
import os
import sys
import subprocess
import shutil


def class_process(source_dir_path, dst_dir_path, types, img_ext, maxSize=1024):
    if not os.path.exists(dst_dir_path):
        os.makedirs(dst_dir_path)

    for file_name in os.listdir(source_dir_path):
        for type in types:
            if type not in file_name:
                continue

        name, ext = os.path.splitext(file_name)

        video_file_path = os.path.join(source_dir_path, file_name)

        cmd = 'ffmpeg -i \"{}\" -qscale:v 2 \"{}/{}_%d.{}\"'.format(video_file_path, dst_dir_path, name,
                                                                            img_ext)

        print(cmd)
        subprocess.call(cmd, shell=True)
        print('\n')




if __name__ == "__main__":
    source_dir_path = os.path.join('data', 'mp4_to_png', 'input')
    dst_dir_path = os.path.join('data', 'mp4_to_png', 'output')

    types = ['.avi', '.mp4']

    img_ext = 'png'

    # for class_name in os.listdir(dir_path):
    class_process(source_dir_path, dst_dir_path, types, img_ext)
    # train_val_split(dst_dir_path, valid_dir_path, class_name, val_part)
