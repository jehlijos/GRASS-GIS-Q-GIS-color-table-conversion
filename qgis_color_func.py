import os
from string import Template


def convert_color_table_grass_to_qgis(table_path, output_path):
    """
      Convert a color table in GRASS GIS format to QGIS format.

      Args:
          table_path (str): Path to the input color table in GRASS format.
          output_path (str): Path to save the output color table in QGIS format.

      Returns:
          None (The function generates an XML file with the updated color palette
           at the specified output path.)

      """

    # Create the directories if they do not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Template for the QGIS color table
    t = Template('''\
    <!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
        <qgis version="3.34.2-Prizren">
      <rasterrenderer opacity="1" alphaBand="0" band="1" type="paletted">
        <rasterTransparency/>
        <colorPalette>
$palette
        </colorPalette>
      </rasterrenderer>
    </qgis>
    ''')

    # Dictionary of color names and their RGB values from GRASS GIS
    color_dict = {
        'aqua': "100 128 255",
        'black': "0 0 0",
        'blue': "0 0 255",
        'brown': "180 77 25",
        'cyan': "0 255 255",
        'gray': "128 128 128",
        'grey': "128 128 128",
        'green': "0 255 0",
        'indigo': "0 128 255",
        'magenta': "255 0 255",
        'orange': "255 128 0",
        'red': "255 0 0",
        'violet': "128 0 255",
        'purple': "128 0 255",
        'white': "255 255 255",
        'yellow': "255 255 0",
    }

    # Open the table
    with open(table_path, 'r') as table:
        table_lines = []
        # replace color names with rgb values
        for line in table:
            for color, rgb in color_dict.items():
                if color in line:
                    line = line.replace(color, rgb)
                    break
            table_lines.append(line)

    # Write the table
    palette = []
    for line in table_lines:
        if line:  # Check if line is not empty
            # skip comment lines
            if line.startswith("#"):
                continue
            # replace : with space
            line = line.replace(":", " ")
            parts = line.split()
            percentage = parts[0]

            #  reformat percentage from 40% to 0.4,
            if "%" in percentage:
                percentage = float(percentage[:-1]) / 100

            rgb_values = tuple(map(int, parts[1:]))
            hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb_values)
            palette.append(
                "        " + f'<paletteEntry value="{percentage}" color="{hex_color}" label="{percentage}"/>' + "\n")

    # Write the output table to the file
    with open(output_path, 'w') as output_table:
        output_table.write(t.substitute(palette="".join(palette)))


if __name__ in ('__main__', '__console__'):
    tables_dir = os.path.dirname(__file__)
    Input = os.path.join(tables_dir, "input_tables", "grass", "corine")
    Output = os.path.join(tables_dir, "output_tables", "qgis", "new_table.qml")
    convert_color_table_grass_to_qgis(Input, Output)
