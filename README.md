# 2024-b-grass-qgis-colors-convert
![example workflow](https://github.com/github/docs/actions/workflows/test_qgis_color_func.yml/badge.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
<br>
**GRASS GIS Color Table Import** <br>
![plugin icon](https://github.com/jehlijos/GRASS-GIS-Q-GIS-color-table-conversion-BACKUP/blob/main/icon.png?raw=true)
<br>
QGIS plugin to load predefined or custom GRASS GIS raster color tables.
> [!NOTE]  
> In this version, the plugin correctly transforms only tables for rasters with absolute values (like Corine Land Cover). <br> For tables with percentage values, absolute values are assigned.
## [Original repository](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert)
## Table of Contents
- [How to Install QGIS Plugin](#how-to-install-qgis-plugin)
- [How to Use Plugin](#how-to-use-plugin)
- [Important Files Description](#important-files-description)

## How to Install QGIS Plugin
- [Download](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/archive/refs/heads/master.zip) this repository in .zip :
    ```
    wget https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/archive/refs/heads/master.zip
    ```
- Add to QGIS: <br>
  Use the video tutorial below <br>
  [![youtube video tutorial](https://i.ytimg.com/vi/AUQouvFyt34/hqdefault.jpg?sqp=-oaymwE2CNACELwBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhsIGwobDAP&rs=AOn4CLBc6EpmZSbGvff1br8hww-28XBWmg)](https://www.youtube.com/watch?v=AUQouvFyt34)

## How to Use Plugin
- Select your raster file from workspace layers or import it from a file. <br>
  ![1](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/1.png?raw=true) <br><br>

- Select a predefined GRASS color table.  <br>
  ![2](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/2.png?raw=true) <br><br>

- Or select a custom GRASS color table from a file.  <br>
  ![3](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/3.png?raw=true) <br><br>

- Preferably save the created QGIS table to a .qml file.  <br>
  ![4](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/4.png?raw=true) <br><br>

- Click run to apply the color table.  <br>
  ![3](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/3.png?raw=true) <br><br>

## Important Files Description
- [qgis_color_func.py](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/blob/master/qgis_color_func.py) - Python file with the function that generates the QML file from the GRASS table file. <br>
- [GRASS_GIS_Color_Table_Import_dockwidget_base.ui](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/blob/master/GRASS_GIS_Color_Table_Import_dockwidget_base.ui) - Qt Designer user interface file. <br>
- [GRASS_GIS_Color_Table_Import_dockwidget.py](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/blob/master/GRASS_GIS_Color_Table_Import_dockwidget.py) - Partly generated file to add functions to widgets in the user interface. <br>
- [test/test_qgis_color_func.py](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/blob/master/test/test_qgis_color_func.py) - Test to generate Corine QML table and compare it with the reference. <br>
