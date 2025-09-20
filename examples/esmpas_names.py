# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 13:50:18 2025

@author: jhbravo
"""

#%%
from earthcmap.loader import escmap_list
dict_cmaps = escmap_list()
dict_cmaps
#%%
### Categories ESMAPS
from earthcmap import escmap_categories
dict_cmaps = escmap_categories()
dict_cmaps
#%%
from earthcmap import escmap_list_by_category
# dict_cmaps = escmap_list_by_category()
dict_cmaps = escmap_list_by_category(category='precipitation')
# dict_cmaps = escmap_list_by_category(category='all')
# dict_cmaps = escmap_list_by_category(category='temperature')
dict_cmaps