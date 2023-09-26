# this was used with the benign files to obtrain the hex representation

from pathlib import Path

def convert_to_bytes(input_file, output_file):
    with open(input_file, 'rb') as f: # open in binary mode
        data = f.read() 
    hex_data = " ".join([f"{byte:02x}" for byte in data]) # convert from binary to hex representation

    with open(output_file, 'w') as f: # write result in output
        f.write(hex_data)

# to make a new directory where the outputs will be stored
current_directory = Path(".")
output_directory = current_directory / "bytes_files"
output_directory.mkdir(exist_ok=True) 

file_extensions = ['.dll', '.exe', '.ocx', '.sys', '.drv'] # only the files with these extension
target_files = [f for f in current_directory.iterdir() if f.suffix in file_extensions]

# conversion process
for file in target_files:
    output_file = output_directory / (file.stem + ".bytes")
    convert_to_bytes(file, output_file)

print(f"Converted {len(target_files)} files to .bytes format.")
