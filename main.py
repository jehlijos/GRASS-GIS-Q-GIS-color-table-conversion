import os


def conversion():
    table_path = r"input_tables\grass\elevation"
    output_path = r"output_tables\qgis\new_table.qml"

    # Create the directories if they do not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Open the table
    table = open(table_path, "r")
    table_lines = table.readlines()
    table.close()

    # Create the output table
    output_table = open(output_path, "a")
    # Clear the file
    output_table.truncate(0)

    qml_header = open("qml_form.txt", "r")

    # Write the header as first 5 lines from the qml_form.txt
    for i in range(5):
        output_table.write(qml_header.readline())

    # Write the table
    val = 1
    for line in table_lines:
        if line.strip():  # Check if line is not empty
            parts = line.split()
            percantage = parts[0]
            rgb_values = tuple(map(int, parts[1:]))
            hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb_values)
            output_table.write("  " + f'<paletteEntry value="{val}" color="{hex_color}" label="{percantage}"/>' + "\n")
            val += 1

    # Add the footer - the rest of the qml_form.txt from line 6
    for line in qml_header:
        output_table.write(line)

    output_table.close()
    qml_header.close()


if __name__ == '__main__':
    conversion()
