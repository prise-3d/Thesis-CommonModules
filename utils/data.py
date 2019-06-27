from modules.utils.config import *

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