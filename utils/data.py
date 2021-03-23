# main imports
import os
import numpy as np
import random

# image processing imports
from PIL import Image

# modules imports
from ..config.cnn_config import *


_scenes_names_prefix   = '_scenes_names'
_scenes_indices_prefix = '_scenes_indices'

# store all variables from current module context
context_vars = vars()

def get_renderer_scenes_indices(renderer_name):

    if renderer_name not in renderer_choices:
        raise ValueError("Unknown renderer name")

    if renderer_name == 'all':
        return scenes_indices
    else:
        return context_vars[renderer_name + _scenes_indices_prefix]

def get_renderer_scenes_names(renderer_name):

    if renderer_name not in renderer_choices:
        raise ValueError("Unknown renderer name")

    if renderer_name == 'all':
        return scenes_names
    else:
        return context_vars[renderer_name + _scenes_names_prefix]


def get_scene_image_quality(img_path):

    # if path getting last element (image name) and extract quality
    img_postfix = img_path.split('/')[-1].split(scene_image_quality_separator)[-1]
    img_quality = img_postfix.replace(scene_image_extension, '')

    return int(img_quality)


def get_scene_image_postfix(img_path):

    # if path getting last element (image name) and extract quality
    img_postfix = img_path.split('/')[-1].split(scene_image_quality_separator)[-1]
    img_quality = img_postfix.replace(scene_image_extension, '')

    return img_quality


def get_scene_image_prefix(img_path):

    # if path getting last element (image name) and extract prefix
    img_prefix = img_path.split('/')[-1].split(scene_image_quality_separator)[0]

    return img_prefix