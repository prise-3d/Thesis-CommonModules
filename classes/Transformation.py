# main imports
import os
import numpy as np

# image processing imports
from ipfml.processing import transform
from ipfml.processing import reconstruction
from ipfml.filters import convolution, kernels
from ipfml import utils

from PIL import Image


# Transformation class to store transformation method of image and get usefull information
class Transformation():

    def __init__(self, _transformation, _param, _size):
        self.transformation = _transformation
        self.param = _param
        self.size = _size

    def getTransformedImage(self, img):

        if self.transformation == 'svd_reconstruction':
            begin, end = list(map(int, self.param.split(',')))
            h, w = list(map(int, self.size.split(',')))
            img_reconstructed = reconstruction.svd(img, [begin, end])
            data_array = np.array(img_reconstructed, 'uint8')

            img_array = Image.fromarray(data_array)
            img_array.thumbnail((h, w))

            data = np.array(img_array)

        if self.transformation == 'ipca_reconstruction':
            n_components, batch_size = list(map(int, self.param.split(',')))
            h, w = list(map(int, self.size.split(',')))
            img_reconstructed = reconstruction.ipca(img, n_components, batch_size)
            data_array = np.array(img_reconstructed, 'uint8')
            
            img_array = Image.fromarray(data_array)
            img_array.thumbnail((h, w))

            data = np.array(img_array)

        if self.transformation == 'fast_ica_reconstruction':
            n_components = self.param
            h, w = list(map(int, self.size.split(',')))
            img_reconstructed = reconstruction.fast_ica(img, n_components)
            data_array = np.array(img_reconstructed, 'uint8')
            
            img_array = Image.fromarray(data_array)
            img_array.thumbnail((h, w))

            data = np.array(img_array)

        if self.transformation == 'min_diff_filter':
            w_size, h_size, stride = list(map(int, self.param.split(',')))
            h, w = list(map(int, self.size.split(',')))

            # bilateral with window of size (`w_size`, `h_size`)
            lab_img = transform.get_LAB_L(img)
    
            img_filter = convolution.convolution2D(lab_img, kernels.min_bilateral_diff, (w_size, h_size), stride)
            diff_array = np.array(img_filter*255, 'uint8')
            diff_img = Image.fromarray(diff_array)
            diff_img.thumbnail((h, w))
        
            data = np.array(diff_img)
            
        if self.transformation == 'static':
            # static content, we keep input as it is
            data = img

        return data
    
    def getTransformationPath(self):

        path = self.transformation

        if self.transformation == 'svd_reconstruction':
            begin, end = list(map(int, self.param.split(',')))
            w, h = list(map(int, self.size.split(',')))
            path = os.path.join(path, str(begin) + '_' + str(end)) + '_S_' + str(w) + '_' + str(h)

        if self.transformation == 'ipca_reconstruction':
            n_components, batch_size = list(map(int, self.param.split(',')))
            w, h = list(map(int, self.size.split(',')))
            path = os.path.join(path, 'N' + str(n_components) + '_' + str(batch_size)) + '_S_' + str(w) + '_' + str(h)

        if self.transformation == 'fast_ica_reconstruction':
            n_components = self.param
            w, h = list(map(int, self.size.split(',')))
            path = os.path.join(path, 'N' + str(n_components)) + '_S_' + str(w) + '_' + str(h)

        if self.transformation == 'min_diff_filter':
            w_size, h_size, stride = list(map(int, self.param.split(',')))
            w, h = list(map(int, self.size.split(',')))
            path = os.path.join(path, 'W_' + str(w_size)) + '_' + str(h_size) + '_Stride_' + str(stride) + '_S_' + str(w) + '_' + str(h)

        if self.transformation == 'static':
            # param contains image name to find for each scene
            path = self.param

        return path

    def getName(self):
        return self.transformation

    def getParam(self):
        return self.param

    def __str__( self ):
        return self.transformation + ' transformation with parameter : ' + self.param