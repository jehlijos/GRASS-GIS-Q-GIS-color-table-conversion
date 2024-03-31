import os


def conversion():
    table_path = r"input_tables\grass\differences"
    output_path = r"output_tables\qgis\new_table.qml"

    # Create the directories if they do not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    color_dict = {
        'black': "0 0 0",
        'yellow': "255 255 0",
        'orange': "255 128 0",
        'red': "255 0 0",
        'magenta': "255 0 255",
        'indigo': "0 128 255",
        'cyan': "0 255 255",
        'green': "0 255 0",
        'white': "255 255 255",
        'grey': "128 128 128",
        'blue': "0 0 255",
        'brown': "180 77 25",
        'violet': "128 0 255",
    }

    # Open the table
    table = open(table_path, "r")
    table_lines = table.readlines()
    table.close()

    # replace color names with rgb values
    for i, line in enumerate(table_lines):
        for color in color_dict:
            if color in line:
                table_lines[i] = line.replace(color, color_dict[color])

    # Create the output table
    output_table = open(output_path, "a")
    # Clear the file
    output_table.truncate(0)

    qml_header = open("qml_form.txt", "r")

    # Write the header as first 5 lines from the qml_form.txt
    for i in range(5):
        output_table.write(qml_header.readline())

    # Write the table

    for line in table_lines:
        if line.strip():  # Check if line is not empty
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

    output_table.close()
    qml_header.close()


if __name__ == '__main__':
    conversion()
