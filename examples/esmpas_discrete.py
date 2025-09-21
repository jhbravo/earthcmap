# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 13:50:18 2025

@author: jhbravo
"""

import numpy as np
import matplotlib.pyplot as plt

from earthcmap import escmap

def escmap_discrete(cmap_name = None, units=None):
    if cmap_name == None:
        cmap_name = "soil_usda"
         
    cmap, norm = escmap(cmap_name)
    
    values = cmap.positions
    
    # Generate random matrix using values from the cbar
    data = np.random.choice(values, size=(10, 10))
    
    # Plot
    fig, ax = plt.subplots(dpi=300)
    img = ax.imshow(data, cmap=cmap, norm=norm)
    plt.title(f"colormap for: {cmap.long_name}")
    
    cbar = plt.colorbar(img)
    ### Middle points
    cbar.set_ticks(cmap.midpositions)
    cbar.set_ticklabels(cmap.midlabels, size=8)
    
    # plt.savefig(f"C:/Users/Ismart/earthcmap/joss/images/{cmap_name}.png", bbox_inches='tight') #uncomment to save figure

# escmap_discrete()
escmap_discrete(cmap_name = "chirps")