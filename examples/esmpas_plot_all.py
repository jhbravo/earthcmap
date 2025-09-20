# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 13:50:18 2025

@author: jhbravo
"""
#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.gridspec import GridSpec
from earthcmap import escmap_list_by_category
from earthcmap import escmap

def plot_escmap_bars():
    """
    Plot all ECSCM: Earth Science data Colormaps,
    displaying each as a horizontal colorbar with its name as a title.
    """
    # categories = ['all', 'atmosphere', 'classic', 'earthobs', 'indices', 'land', 'ocean', 'precipitation', 'temperature']
    dict_cmaps = escmap_list_by_category(category='all')

    all_cmaps = []
    for key, values in dict_cmaps.items():
        if not 'classic' in key:
            all_cmaps.append(key)
            all_cmaps.extend(values)
    # print(all_cmaps)

    cmap_names = all_cmaps
    num_cmaps = len(cmap_names)

    n_rows = 15
    n_cols = (num_cmaps + n_rows - 1) // n_rows  # ceil division
    fig = plt.figure(figsize=(n_cols * 4, 15), dpi=300, facecolor='white')
    grid = GridSpec(n_rows, n_cols, hspace=0.6, wspace=0.5)

    for idx, cmap_name in enumerate(cmap_names):
        row = idx % n_rows
        col = idx // n_rows
        ax = fig.add_subplot(grid[row, col])
        
        try:
            cmap, norm = escmap(cmap_name)
            mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation='horizontal' )
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_title(cmap.long_name, fontsize=10, pad=6)
        except ValueError:
            # If the colormap is not found, use a white cmap and mark the name
            cmap = mpl.colors.ListedColormap(['white'])
            ax.text(0.5, 0.5, f"{cmap_name} colormaps",
                    ha='center', va='center', fontsize=16, color='black',
                    transform=ax.transAxes)
            ax.axis('off')
            
    fig.suptitle("Earth Science data Colormaps", fontsize=18, y=0.91)
    plt.savefig("C:/Users/Ismart/earthcmap/joss/images/plot_escmap_barsaps.png", bbox_inches='tight') #uncomment to save figure
    plt.show()
    
plot_escmap_bars()
