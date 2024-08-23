import os
import subprocess

def convert_ui_to_py(input_file, output_file):
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return

    # Command to convert .ui to .py
    command = f"pyuic5 -x {input_file} -o {output_file}"

    # Run the command
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully converted {input_file} to {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    input_file = './ui.ui'
    output_file = 'ui.py'
    convert_ui_to_py(input_file, output_file)
