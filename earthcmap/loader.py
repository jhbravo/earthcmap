# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 13:48:09 2025

@author: jhbravo
"""
from matplotlib.colors import ListedColormap, BoundaryNorm, LinearSegmentedColormap, Normalize
import json
import os

def get_lits_files(search_paths=None):
    """
    Retrieve a color map by name from available JSON files.

    Parameters:
        name (str): Name of the color map (e.g., "ir4").
        search_paths (list): Optional list of JSON file paths to search.

    Returns:
        dict: A dictionary with 'type', 'values', and 'colors'.
    """
    if search_paths is None:
        base_dir = os.path.join(os.path.dirname(__file__), "cmaps")
        search_paths = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.endswith(".json")]
    return search_paths

def get_cmap_name(name, search_paths=None):
    """
    Retrieve a color map by name from available JSON files.

    Parameters:
        name (str): Name of the color map (e.g., "ir4").
        search_paths (list): Optional list of JSON file paths to search.

    Returns:
        dict: A dictionary with 'type', 'values', and 'colors'.
    """
    search_paths = get_lits_files()

    for path in search_paths:
        with open(path, "r") as f:
            data = json.load(f)
            if name in data:
                return data[name]

    raise ValueError(f"Color map '{name}' not found in provided JSON files.")

def escmap_list():
    """
    List all available color map names from JSON files in the 'cmaps' directory.

    Returns:
        list: A list of unique color map names.
    """

    search_paths = get_lits_files()
    cmap_names = {}

    for path in search_paths:
        # print(path)
        with open(path, "r") as f:
            data = json.load(f)
            nfile = os.path.basename(path)[:-5]
            cmap_names.update({nfile:list(data.keys())})
    
    return cmap_names

# 
def escmap_categories():
    """
    List all available color map names from JSON files in the 'cmaps' directory.

    Returns:
        list: A list of unique color map names.
    """

    search_paths = get_lits_files()
    cmap_names = []

    for path in search_paths:
        nfile = os.path.basename(path)[:-5]
        cmap_names.append(nfile)
    
    return cmap_names
    
# 
def escmap_list_by_category(category=None):
    """
    List all available color map names from JSON files in the 'cmaps' directory.

    Returns:
        list: A list of unique color map names.
    """
    if category == None:
        category='earthobs'

    search_paths = get_lits_files()
    cmap_names = {}

    for path in search_paths:
        # print(path)
        nfile = os.path.basename(path)[:-5]
        
        # if category == 'all':
        #     category = nfile
        # print(category,nfile)
        if category == nfile:
            with open(path, "r") as f:
                data = json.load(f)
                cmap_names.update({nfile:list(data.keys())})
        elif category == 'all':
            with open(path, "r") as f:
                data = json.load(f)
                cmap_names.update({nfile:list(data.keys())})
    
    return cmap_names

#### main
def newmaxmin(old_val, old_max, old_min):      
    new_val = (old_val - old_min) / (old_max - old_min)
    return round(new_val, 2)

def escmap(cmap_name, extend='neither'):
    """
    Returns a cmap and norm for a registered colormap name.
    
    Parameters:
        name (str): Name of the predefined colormap ('cmap_name1', etc.).
        extend (str): How to handle values beyond the range ('neither', 'min', 'max', 'both').
        
    Returns:
        cmap (ListedColormap), norm (BoundaryNorm)
    """
    # cmap_name = "prec01"
    entry = get_cmap_name(cmap_name)
    
    cmaptype = entry["type"]
    
    values = [x[0] for x in entry['data']]
    colors = [x[1] for x in entry['data']]
    labels = [x[2] for x in entry['data']]
    
    v_min = min(values)
    v_max = max(values)
    
    if cmaptype == "discrete":
        ### this is to add a extended data to display the entine colors  ###
        values += [values[-1] * 2]
        colors += [colors[-1]]
        labels += [f"> {labels[-1]}"]
        ### ------------------------------------------------------------ ###
        # Create colormap and norm
        cmap = ListedColormap(colors, name = cmap_name)
        norm = BoundaryNorm(values, len(colors))
        # Calculate midpoints for labels
        midpos = [(values[i] + values[i + 1]) / 2 for i in range(len(values) - 1)]
        cmap.midpositions = midpos
        cmap.midlabels = labels[:-1]
        
    elif cmaptype == "continuous":
        merged_colors = [(newmaxmin(x[0], v_max, v_min),x[1]) for x in zip(values, colors)]
        # Create colormap and norm
        nval = entry["N"]
        cmap = LinearSegmentedColormap.from_list(cmap_name, merged_colors, N = nval)
        norm = Normalize(vmin = v_min, vmax = v_max, clip = False)
        
    cmap.units = entry["units"]
    cmap.long_name = entry["long_name"]
    cmap.positions = values
    cmap.labels = labels
    
    return cmap, norm































