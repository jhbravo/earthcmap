# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 13:50:18 2025

@author: jhbravo
"""

import numpy as np
import matplotlib.pyplot as plt

from earthcmap import escmap

def escmap_discrete(cmap_name = None):
    if cmap_name == None:
        cmap_name = "cira_ir108"
         
    cmap, norm = escmap(cmap_name)
    
    values = cmap.positions
    
    # Generate random matrix using values from the cbar
    data = np.random.choice(values, size=(10, 10),)
    
    # Plot
    fig, ax = plt.subplots(dpi=300)
    img = ax.imshow(data, cmap=cmap, norm=norm)
    plt.title(f"colormap for: {cmap.long_name}")
    
    cbar = plt.colorbar(img)

    cbar.set_ticks(cmap.positions)
    cbar.set_ticklabels(cmap.labels)
    
    plt.savefig(f"/joss/images/{cmap_name}.png", bbox_inches='tight')

# escmap_discrete()
escmap_discrete(cmap_name = "ndvi_msg")