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

# def convert_units(values, old_units, new_units):
#     # Normalize input
#     old_units = old_units.strip().lower()
#     new_units = new_units.strip().lower()

#     # Return unchanged if units are the same
#     if old_units == new_units:
#         return values

#     # Define conversion functions
#     def c_to_k(x): return round(x + 273.15, 2)
#     def k_to_c(x): return round(x - 273.15, 2)
#     def c_to_wm2(x): return round(5.6693E-8 * ((x + 273.15) ** 4), 2)
#     def in_to_mm(x): return round(x * 25.4, 2)
#     def mm_to_in(x): return round(x / 25.4, 2)

#     # Mapping of unit conversions
#     conversion_map = {
#         ("c", "k"): c_to_k,
#         ("k", "c"): k_to_c,
#         ("c", "w m^{-2}"): c_to_wm2,
#         ("in", "mm"): in_to_mm,
#         ("mm", "in"): mm_to_in,
#     }

#     key = (old_units, new_units)

#     if key not in conversion_map:
#         raise ValueError(f"Unsupported conversion: {old_units} → {new_units}")

#     func = conversion_map[key]
#     return [func(x) for x in values]

def convert_units(values, old_units, new_units):
    if old_units == new_units:
        return values
    else:
        if old_units == "C" and new_units == "K":
            values = [round(x + 273.15, 2) for x in values]
        elif old_units == "K" and new_units == "C":
            values = [round(x - 273.15, 2) for x in values]
        elif old_units == "C" and new_units == "W m^{-2}":
            values = [round(5.6693E-8*((x + 273.15)**4), 2) for x in values]
        elif old_units == "K" and new_units == "W m^{-2}":
            values = [round(5.6693E-8*(x**4), 2) for x in values]
        elif old_units == "in" and new_units == "mm":
            values = [round(x * 25.4, 2) for x in values]
        elif old_units == "mm" and new_units == "in":
            values = [round(x / 25.4, 2) for x in values]
        elif old_units in ["m s^{-1}","m s-1"] and new_units == "Kt":
            values = [round(x / 0.514444, 2) for x in values]    
        elif old_units == "Kt" and new_units == "m s^{-1}":
            values = [round(x * 0.514444, 2) for x in values]    
        return values
    

def escmap(cmap_name, units=None):
    """
    Returns a cmap and norm for a registered colormap name.
    
    Parameters:
        name (str): Name of the predefined colormap ('cmap_name1', etc.).
        unist (str): Reconfigure based on changing the values if the unist are differents.
        
    Returns:
        cmap (ListedColormap), norm (BoundaryNorm)
    """
    # cmap_name = "prec01"
    entry = get_cmap_name(cmap_name)
    
    cmaptype = entry["type"]
    
    values = [x[0] for x in entry['data']]
    colors = [x[1] for x in entry['data']]
    labels = [x[2] for x in entry['data']]
    
    if units == None or units == entry["units"]:
        out_units = entry["units"]
    elif units != entry["units"]:
        values = convert_units(values, entry["units"], units)
        out_units = units
            
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
        
    cmap.units = out_units
    cmap.long_name = entry["long_name"]
    cmap.positions = values
    cmap.labels = labels
    
    return cmap, norm





























