---
title: 'ESCMAP: Earth Science data Colormaps'
tags:
  - Earth science
  - data visualization
  - colormaps
  - plotting
  - Python
authors:
  - name: Jorge Humberto Bravo Mendez
    orcid: 0009-0005-0561-150X
    equal-contrib: true
    affiliation: "1"
affiliations:
 - name: Stevens Institute of Technology, United States
   index: 1
date: 20 September 2025
bibliography: paper.bib
---

# Summary

To represent scientific data, a wide variety of colormaps are available to enhance visual interpretation. However, in Earth sciences, these general-purpose colormaps, while useful for quick visualization, are not always suitable for presenting final results. In fields such as meteorology and remote sensing, it's common practice to compare or validate research outputs against official datasets or institutional products from official sources. For meaningful comparisons, using the same colormaps as those official sources is often essential. This library compiles some of the most commonly used colormaps in these domains, offering more consistent and appropriate visualizations when aligning with existing products.

# Statement of need

In Earth Sciences, effective data visualization is fundamental to interpreting and communicating the outputs of numerical models and satellite observations. Fields such as meteorology and atmospheric science have a long-standing reliance on visualization techniques to convey complex data [@may_metpy_2022]. As scientific data becomes increasingly visible to the general public, particularly in widely consumed applications such as weather forecasts and hazard maps, colormaps serve as a crucial interface between science and public communication [crameri_misuse_2020], that why the use of rights  colormaps is particularly critical, as they significantly affect how patterns, gradients, and anomalies are perceived and understood. 

While many tools are available for exploring Earth science data, Python, the language used to develop this library, is widely used across geoscientific applications [@trauth_python_2024] and has seen broad adoption within the Earth sciences community. What began as a tool favored by early adopters has since evolved into a mainstream language, now supported by major research institutions and integrated into a wide range of scientific workflows. Its popularity stems from a combination of readable syntax, a vast ecosystem of scientific libraries, and the ability to integrate seamlessly with data formats and computational tools commonly used in atmospheric, oceanic, and climate research [@lin_why_2012]. Today, Python plays a central role in advancing reproducible, efficient, and scalable workflows across a growing number of Earth science applications.

On many occasions, it's common practice to compare or validate research outputs against official datasets or institutional products from official sources, so using same colormap helps make a quick, qualitative visual comparison. 

Given Python's popularity and the importance of selecting appropriate colormaps, several libraries have been developed to extend or improve upon the standard options. For instance, libraries like cmap [@akhmerov_cmap_2025] offer general-purpose colormap extensions, or colorspace, a Python Toolbox for Manipulating and Assessing Colors and Palettes [@stauffer_colorspace_2024], while CMasher provides scientifically designed alternatives focused on perceptual accuracy and clarity [@velden_cmasher_2020]. Other packages are tailored to specific types of data, such as Herbie, which retrieves recent and historical numerical weather prediction model outputs from various cloud-based archives  [@blaylock_herbie_2025], or MetPy, a comprehensive toolkit for reading, visualizing, and analyzing meteorological data [@may_metpy_2016]. While these specialized libraries often include their own custom colormaps, they typically come bundled with extensive functionality. As a result, if all you need is access to the colormaps, installing an entire domain-specific or complex library can be excessive or impractical.

This project aims to standardize the use of colormaps across disciplines such as meteorology, oceanography, and remote sensing among others by offering a curated library of the most commonly used colormaps from high-impact institutions and agencies (e.g., NOAA, NASA, ECMWF).

This is important because adopting well-established colormaps preserves continuity in how information is interpreted. Even small changes in color design can break users’ visual expectations, obscure patterns they are accustomed to recognizing, or undermine trust in the data. By aligning with widely used and widely learned color conventions, the project helps maintain a shared visual language that supports clarity, consistency, and reliable interpretation across applications [@datavist_colour_2025].

# ESCMAP

The ESCMAP package offers a curated collection of colormaps specifically designed for Earth sciences, as illustrated in Figure 1. Built in Python and relying solely on matplotlib [@hunter_matplotlib_2007] as its only dependency, the library is lightweight and easy to integrate. It is intended to complement other scientific libraries by providing appropriate colormaps along with their corresponding normalization settings. The goal is to streamline the visualization process for researchers, reducing the time spent selecting or customizing colormaps, while promoting consistency and accuracy in the presentation of Earth science data.

Each colormap in the library is:
* Inspired by real-world usage, based on high-impact institutions or research publications.
* Documented with source information, including credits and context for its use.
* The colormaps are based on JSON files, allowing easy readability

Unlike other tools or libraries, this package generates colormaps using a minimal set of key colors. Each colormap is defined in a JSON file that specifies the breakpoint values, corresponding colors, and optional labels. These values represent the physical variable the colormap is designed for and are used to construct the color scale accurately, as illustrated in Figure 2. The JSON files are organized into thematic categories: `['atmosphere', 'earthobs', 'indices', 'land', 'ocean', 'precipitation', 'temperature']`. The package supports two types of colormaps: continuous and discrete.

# Example Usage

Using the package is straightforward: simply import the function and call it to retrieve the colormap and its corresponding normalization, as shown in the Python example below. Figures 3 and 4 display the resulting visualizations.

``` python
from earthcmap import escmap

cmap, norm = escmap("your escmap choice")
```

The following two examples demonstrate how to use the colormaps shown in Figure 2. In both cases, a random NumPy matrix was generated based on the value range defined in each respective colormap to ensure appropriate visualization.

## Discrete 

``` python 
import numpy as np
import matplotlib.pyplot as plt

from earthcmap import escmap

cmap, norm = escmap("chirps")

values = cmap.positions

# Generate random matrix using values from the cbar
data = np.random.choice(values, size=(10, 10))

# Plot
fig, ax = plt.subplots(dpi=300)
img = ax.imshow(data, cmap=cmap, norm=norm)
plt.title(f"colormap for: {cmap.long_name}")

cbar = plt.colorbar(img)

cbar.set_ticks(cmap.midpositions)
cbar.set_ticklabels(cmap.midlabels, size=8)
```

## Continuous

``` python 
import numpy as np
import matplotlib.pyplot as plt

from earthcmap import escmap

cmap, norm = escmap("cira_ir108")

values = cmap.positions

# Generate random matrix using values from the cbar
data = np.random.choice(values, size=(10, 10))

# Plot
fig, ax = plt.subplots(dpi=300)
img = ax.imshow(data, cmap=cmap, norm=norm)
plt.title(f"colormap for: {cmap.long_name}")

cbar = plt.colorbar(img)

cbar.set_ticks(cmap.positions)
cbar.set_ticklabels(cmap.labels)
```

# Real data examples

As a practical use case, we employ data from the Model for Prediction Across Scales–Atmosphere (MPAS-A). Figures 5 and 6 demonstrate the use of escmap, in combination with the MPAS-Viewer library, to efficiently visualize MPAS-A data [@mendez_mpas-viewer_2026] over New York Metropolitan Area City and its surrounding regions. The application of standardized colormaps makes the data immediately more interpretable. Furthermore, regardless of changes in the model domain or the use of different datasets, equivalent variables are rendered consistently using the same colormap parameters, ensuring visual consistency and comparability. Figure 5 showcases colormaps from the `land` categories, while Figure 6 includes examples from the `precipitation` and  `temperature` categories.

# Benefits

This library provides access to colormaps commonly used by official institutions, as well as others designed for clearer and more intuitive interpretation. It helps avoid the ambiguity of choosing an appropriate colormap by offering ready-to-use, standardized options. As a result, visualizations remain consistent and aligned with recognized practices, ensuring clarity and comparability across maps and datasets.

# Future Work

This library includes a collection of colormaps that I have gathered and used over the years. During my PhD, the need to organize and share them for broader use became increasingly clear. Moving forward, contributions from others familiar with colormap design are welcome—whether by submitting new colormaps directly (with proper credit) or by contacting me to include them in the library.

# Figures

![Figure 1](/joss/images/plot_escmap_barsaps.png)

*Figure 1: Figure 2: List of colormaps available in the initial version of this library, organized by category alongside their corresponding colormaps.*

![Figure 2](/joss/images/json_example.png)

*Figure 2: Base structure for generating colormaps: the left panel shows the structure for creating discrete colormaps, while the right panel illustrates the structure for continuous colormaps.*

![Figure 3](/joss/images/chirps.png)

*Figure 3: Example demonstrating the use of a discrete colormap.*

![Figure 4](/joss/images/cira_ir108.png)

*Figure 4: Example demonstrating the use of a continuous colormap.*

![Figure 5](/joss/images/imgs_01.png)

*Figure 5: MPAS model static variables. Top left: terrain elevation; top right: vegetation category; bottom left: dominant soil category; bottom right: land–ocean mask.*

![Figure 6](/joss/images/imgs_02.png)

*Figure 6: MPAS model output variables. Top left: radar reflectivity; top right: OLR; bottom left: precipitation; bottom right: 2-meter temperature.*

# References