import os
import numpy as np
import tifffile as tiff
import skimage
import imageio as iio

import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset as BaseDataset
import albumentations as albu

def center_crop(imm, size, imtype = 'image'):
    h = int(size[0]/2)
    w = int(size[1]/2)
    ch = int(imm.shape[0]/2)
    cw = int(imm.shape[1]/2)
    if imtype == 'image':
        return imm[ch-h:ch+h, cw-w:cw+w, :]
    else:
        return imm[ch-h:ch+h, cw-w:cw+w]

class Dataset(BaseDataset):
    """Read images, apply augmentation and preprocessing transformations.    
    """
    
    def __init__(
            self, 
            root,
            augmentation= False,
    ):
     
        self.t1_images_dir = os.path.join(root, '2010/')
        self.t2_images_dir = os.path.join(root, '2017/')
        self.masks2d_dir = os.path.join(root, '2D/')
        self.masks3d_dir = os.path.join(root, '3D/')
        self.ids = os.listdir(self.t1_images_dir)
        self.idm = os.listdir(self.masks3d_dir)

        self.t1_images_fps = [os.path.join(self.t1_images_dir, image_id) for image_id in self.ids]
        self.t2_images_fps = [os.path.join(self.t2_images_dir, image_id) for image_id in self.ids]
        self.masks2d_fps = [os.path.join(self.masks2d_dir, image_id) for image_id in self.ids]
        self.masks3d_fps = [os.path.join(self.masks3d_dir, image_id) for image_id in self.idm]  

        self.augmentation = augmentation

    def __getitem__(self, i):
        
        # read data with tifffile because of 3d mask int16
        t1 = iio.imread(self.t1_images_fps[i])#.transpose([2,0,1])
        t2 = iio.imread(self.t2_images_fps[i])#.transpose([2,0,1])
        mask2d = iio.imread(self.masks2d_fps[i])
        mask3d = tiff.imread(self.masks3d_fps[i])

        # apply augmentations
        if self.augmentation:
            sample = self.augmentation(image=t1, t2=t2, mask=mask2d, mask3d=mask3d)
            t1, t2, mask2d, mask3d = sample['image'], sample['t2'], sample['mask'], sample['mask3d']
        
        return t1, t2, mask2d, mask3d 

        
    def __len__(self):
        return len(self.ids)