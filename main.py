import os
import shutil

def find_people(name,gallery):
    if not os.path.exists(f'/label_photos/{ name }'):
        return None
    else:
        #photos = os.listdir(f'/label_photos/{ name }')
        photos_w_person = os.popen(f'face-recognition /label_photos/{ name } { gallery }').read()

def add_photo2find(name,photo):
    # test if exist folder with NAME name else create
    if not os.path.exists(f'/label_photos/{ name }'):
        os.makedirs(f'/label_photos/{ name }')
    # mv photo to this folder
    photos = os.listdir(f'/label_photos/{ name }')
    shutil.move(photo,f'/label_photos/{ name }/{ name }[{ len(photos) }]{ photo.split(".")[-1] }')


def all_photos(path):  
    return os.listdir(f'/label_photos/{ name }')

def main():
    pass
main()
