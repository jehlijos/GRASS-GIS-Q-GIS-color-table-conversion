# 2024-b-grass-qgis-colors-convert
![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)]([https://www.gnu.org/licenses/gpl-3.0)
<br>
**GRASS GIS Color Table Import** <br>
![plugin icon](https://github.com/jehlijos/GRASS-GIS-Q-GIS-color-table-conversion-BACKUP/blob/main/icon.png?raw=true)
<br>
QGIS plugin to load predefined or custom GRASS GIS raster color tables.
> [!NOTE]  
> At this version plugin correctly transforms only tables for rasters with absolute values (like Corine Land Cover). <br> To tables with percentual values are assinged absolute values.

## Table of contents

## How to install QGIS plugin
- clone this repository:
```
git clone https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert
```
- add to QGIS: <br>
use video tutorial below <br>
  [![youtube video tutorial](https://i.ytimg.com/vi/AUQouvFyt34/hqdefault.jpg?sqp=-oaymwE2CNACELwBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhsIGwobDAP&rs=AOn4CLBc6EpmZSbGvff1br8hww-28XBWmg)](https://www.youtube.com/watch?v=AUQouvFyt34)
## How to use plugin
- Select your raster file from workspace layers or import it from file. <br>
  ![1](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/1.png?raw=true) <br><br>

- Select predefined GRASS color table.  <br>
  ![2](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/2.png?raw=true) <br><br>

- Or select custom GRASS color table from file.  <br>
  ![3](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/3.png?raw=true) <br><br>

- Preferably save created QGIS table to .qml file.  <br>
  ![4](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/4.png?raw=true) <br><br>

- Click run to apply the color table.  <br>
  ![3](https://github.com/jehlijos/josef-jehlicka/blob/main/schoolwork/FGISPHOTO/3.png?raw=true) <br><br>

## Important Files description <br>
- [qgis_color_func.py] - python file with function](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/blob/master/qgis_color_func.py) that generates QML file from GRASS table file. <br>
- [GRASS_GIS_Color_Table_Import_dockwidget_base.ui](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/blob/master/GRASS_GIS_Color_Table_Import_dockwidget_base.ui) - Qt Designer user interferce file. <br>
- [GRASS_GIS_Color_Table_Import_dockwidget.py](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/blob/master/GRASS_GIS_Color_Table_Import_dockwidget.py) - Partly generated file to add functions to widgets in user interface <br>
- [test/test_qgis_color_func.py](https://github.com/ctu-fgis/2024-b-grass-qgis-colors-convert/blob/master/test/test_qgis_color_func.py) - test to generate Corine QML table and compare it wwith reference. <br>

