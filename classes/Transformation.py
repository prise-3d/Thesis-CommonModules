import os

from ipfml.processing import reconstruction

# Transformation class to store transformation method of image and get usefull information
class Transformation():

    def __init__(self, _transformation, _param):
        self.transformation = _transformation
        self.param = _param

    def getTransformedImage(self, img):

        if self.transformation == 'svd_reconstruction':
            begin, end = list(map(int, self.param.split(',')))
            data = reconstruction.svd(img, [begin, end])

        if self.transformation == 'ipca_reconstruction':
            n_components, batch_size = list(map(int, self.param.split(',')))
            data = reconstruction.ipca(img, n_components, batch_size)

        if self.transformation == 'fast_ica_reconstruction':
            n_components = self.param
            data = reconstruction.fast_ica(img, n_components)

        if self.transformation == 'static':
            # static content, we keep input as it is
            data = img

        return data
    
    def getTransformationPath(self):

        path = self.transformation

        if self.transformation == 'svd_reconstruction':
            begin, end = list(map(int, self.param.split(',')))
            path = os.path.join(path, str(begin) + '_' + str(end))

        if self.transformation == 'ipca_reconstruction':
            n_components, batch_size = list(map(int, self.param.split(',')))
            path = os.path.join(path, 'N' + str(n_components) + '_' + str(batch_size))

        if self.transformation == 'fast_ica_reconstruction':
            n_components = self.param
            path = os.path.join(path, 'N' + str(n_components))

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