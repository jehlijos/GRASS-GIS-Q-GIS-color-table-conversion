import os


def conversion(table_path, output_path):
    # Create the directories if they do not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

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
        table_lines = table.readlines()

    # replace color names with rgb values
    for i, line in enumerate(table_lines):
        for color in color_dict:
            if color in line:
                table_lines[i] = line.replace(color, color_dict[color])

    # Create the output table
    with open(output_path, 'w') as output_table:
        qml_header = open("qml_form", "r")

        # Write the header as first 5 lines from the qml_form file
        for i in range(5):
            output_table.write(qml_header.readline())

        # Write the table
        for line in table_lines:
            if line:  # Check if line is not empty
                # replace : with space
                line = line.replace(":", " ")
                parts = line.split()
                percantage = parts[0]

                # refromat percantage from 40% to 0.4
                if "%" in percantage:
                    percantage = int(percantage[:-1]) / 100

                rgb_values = tuple(map(int, parts[1:]))
                hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb_values)
                output_table.write(
                    "  " + f'<paletteEntry value="{percantage}" color="{hex_color}" label="{percantage}"/>' + "\n")

        # Add the footer - the rest of the qml_form.txt from line 6
        for line in qml_header:
            output_table.write(line)

        qml_header.close()


if __name__ == '__main__':
    Input = r"input_tables\grass\corine"
    Output = r"output_tables\qgis\new_table.qml"
    conversion(Input, Output)
