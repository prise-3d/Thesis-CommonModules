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


def augmented_data_image(block, output_folder, prefix_image_name):

    rotations = [0, 90, 180, 270]
    img_flip_labels = ['original', 'horizontal', 'vertical', 'both']

    horizontal_img = block.transpose(Image.FLIP_LEFT_RIGHT)
    vertical_img = block.transpose(Image.FLIP_TOP_BOTTOM)
    both_img = block.transpose(Image.TRANSPOSE)

    flip_images = [block, horizontal_img, vertical_img, both_img]

    # rotate and flip image to increase dataset size
    for id, flip in enumerate(flip_images):
        for rotation in rotations:
            rotated_output_img = flip.rotate(rotation)

            output_reconstructed_filename = prefix_image_name + post_image_name_separator
            output_reconstructed_filename = output_reconstructed_filename + img_flip_labels[id] + '_' + str(rotation) + '.png'
            output_reconstructed_path = os.path.join(output_folder, output_reconstructed_filename)

            if not os.path.exists(output_reconstructed_path):
                rotated_output_img.save(output_reconstructed_path)


def remove_pixel(img, limit):
    
    width, height = img.shape
    
    output = np.zeros((width, height))
    
    for i in range(width):
        for j in range(height):
            
            if img[i,j] <= limit:
                output[i,j] = img[i,j]
                
    return output


def get_random_value(distribution):
    rand = random.uniform(0, 1)
    prob_sum = 0.
    
    for id, prob in enumerate(distribution):
        
        prob_sum += prob
        
        if prob_sum >= rand:
            return id
        
    return len(distribution) - 1


def distribution_from_data(data):
    
    occurences = np.array([data.count(x) for x in set(data)])
    max_occurences = sum(occurences)
    
    return occurences / max_occurences


def fill_image_with_rand_value(img, func, value_to_replace):
    
    width, height = img.shape
    
    output = np.zeros((width, height))
    
    for i in range(width):
        for j in range(height):
            
            if img[i,j] == value_to_replace:
                output[i, j] = func()
            else:
                output[i, j] = img[i, j]
                
    return output