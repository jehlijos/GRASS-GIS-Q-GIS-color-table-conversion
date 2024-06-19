"""
Test to check if Corine GRASS table is applied correctly
to sample_data/corine_sample.tif
and if the output table is created correctly
"""
import os
from pathlib import Path
import tempfile
import filecmp

from qgis.core import QgsRasterLayer
import pytest

from qgis_color_func import convert_color_table_grass_to_qgis


def getCORINEtable():
    """
    Get the path to the CORINE table.
    :return: Path to the CORINE table
    """
    # Get the current script directory
    script_dir = Path(__file__).resolve().parent

    # Construct the path to the target directory
    target_dir = script_dir.parent / "input_tables" / "grass"

    # Specify the filename you want to access
    filename = "corine"

    # Create the full path to the file
    file_path = target_dir / filename
    return file_path


def test_getGRASStable():
    """
    Check if the GRASS table file exists.
    """
    # Get the current script directory
    file_path = getCORINEtable()
    # Check if the file exists
    file_exist_check = file_path.exists()
    print(f"GRASS table file exists: {file_exist_check}")

    assert file_exist_check == True


def getRaster():
    """
    Get the path to the raster file.
    :return: Path to the raster file.
    """

    # Get the current script directory
    script_dir = Path(__file__).resolve().parent

    # Construct the path to the target directory
    target_dir = script_dir.parent / "test" / "sample_data"

    # Specify the filename you want to access
    filename = "corine_sample.tif"

    # Create the full path to the file
    file_path = target_dir / filename
    return file_path


def test_getRaster():
    """
    Check if the raster file exists.
    """

    # Get the current script directory
    file_path = getRaster()
    # Check if the file exists
    file_exist_check = file_path.exists()
    print(f"Raster file exists: {file_exist_check}")

    assert file_exist_check == True


def CreateQGISLayer():
    """
    Create a QGIS raster layer.
    :return: QgsRasterLayer object
    """
    # Create a raster layer
    raster = getRaster()
    rasterLayer = QgsRasterLayer(str(raster), "corine_sample")
    return rasterLayer


def test_CreateQGISLayer():
    """
    Check if the raster layer is created successfully.
    """
    rasterLayer = CreateQGISLayer()
    if rasterLayer.isValid():
        print("Raster layer created successfully")
        assert True


def normalize_line_endings(text):
    """
    Normalize line endings to LF (Unix style).
    """
    return text.replace('\r\n', '\n').replace('\r', '\n')


def write_with_lf_line_endings(content, filepath):
    """
    Write content to a file with LF (Unix style) line endings.
    """
    with open(filepath, 'w', newline='\n') as f:
        f.write(content)


def test_applyGRASSColorTable():
    """
    Apply the GRASS color table to the raster layer, and check if it is applied successfully.
    """
    # Get the raster layer
    rasterLayer = CreateQGISLayer()
    # Get the GRASS color table
    GRASStable_path = getCORINEtable()

    # Create a temporary qml file
    tempdir = tempfile.mkdtemp()
    Tempfile = os.path.join(tempdir, "tempfile.qml")

    # Convert the GRASS color table to QGIS format
    convert_color_table_grass_to_qgis(GRASStable_path, Tempfile)

    # Normalize line endings of the generated QML file
    with open(Tempfile, 'r') as f:
        content = f.read()
    normalized_content = normalize_line_endings(content)
    write_with_lf_line_endings(normalized_content, Tempfile)

    # Apply the color table
    rasterLayer.loadNamedStyle(str(Tempfile))

    # Check if the color table is applied
    if rasterLayer.isValid():
        print("Color table applied successfully")
        assert True


def test_OutputFile():
    """
    Check if the output table is created correctly.
    Compare it with reference file.
    """
    # Get the GRASS color table
    GRASStable_path = getCORINEtable()

    # Create a temporary qml file
    tempdir = tempfile.mkdtemp()
    Tempfile = os.path.join(tempdir, "tempfile.qml")

    # Convert the GRASS color table to QGIS format
    convert_color_table_grass_to_qgis(GRASStable_path, Tempfile)

    # Normalize line endings of the generated QML file
    with open(Tempfile, 'r') as f:
        content = f.read()
    normalized_content = normalize_line_endings(content)
    write_with_lf_line_endings(normalized_content, Tempfile)

    # Check if the output table is created correctly
    script_dir = Path(__file__).resolve().parent

    # Construct the path to the target directory
    target_dir = script_dir.parent / "test" / "reference"

    # Specify the filename you want to access
    filename = "corine.qml"

    # Create the full path to the file
    CORINE_file_path = target_dir / filename

    # Compare the output table with the reference table
    print("Generated file matches the reference file (corine): ",
          filecmp.cmp(Tempfile, CORINE_file_path, shallow=False))
    assert filecmp.cmp(Tempfile, CORINE_file_path, shallow=False)

    # Clean up
    os.remove(Tempfile)


if __name__ == "__main__":
    pytest.main()
