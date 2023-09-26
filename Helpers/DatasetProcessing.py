# this script was used on the binary files to create the greyscales

import os
import numpy as np
import torchvision.transforms as transforms
from PIL import Image

IMAGE_SIZE = 224 
DATA_DIR = '.' # were to take the files from
OUTPUT_DIR = '.\\Greyscales' # were to output the greyscales
PROCESSED_LOG = 'processed_files.txt' # log gile to save progress

# helper function to check for log file, if there is one, check contents to resume process
if os.path.exists(PROCESSED_LOG):
    with open(PROCESSED_LOG, 'r') as f:
        processed_files = set(f.read().splitlines())
else:
    processed_files = set()

def read_bytes(filepath):
    with open(filepath, 'r') as f:
        hex_values = f.read().split()[1:] # read contents of the file, split, and skip header
        byte_values = [int(val, 16) for val in hex_values if val != '??'] # convert each hex value to its int repres and skipping values that are '??'(I ran into some errors due to '??')
        return np.array(byte_values, dtype=np.uint8) # convert list to unsigned 8-bit int array
    
def visualize_data(image_array, initial_filename, resized = False):
    filename = initial_filename
    if resized is True:
        filename = filename + "_resized"
    
    pil_image = Image.fromarray(image_array, 'L') # convert byte array to greyscale
    transformed_image = transform(pil_image) # convert to tensor and apply normalization 
    save_image = transforms.ToPILImage()(transformed_image) # convert back to image
    output_filename = os.path.splitext(filename)[0] + '.png' #remove .bytes and add .png
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    save_image.save(output_path)
    
def initial_size(data, fixed_width):
    return np.reshape(data, (fixed_width, -1))

# modify the files size
def handle_size(data, image_size):
    if len(data) > image_size * image_size: # check if the 
        return data[:image_size * image_size].reshape((image_size, image_size)) # truncate
    else:
        padded_data = np.pad(data, (0, image_size * image_size - len(data)), 'constant', constant_values=0) # pad
        return padded_data.reshape((image_size, image_size))

# make dir for outputs
os.makedirs(OUTPUT_DIR, exist_ok=True)

# transformations
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5]) # I normalized the tensor to have a mean of 0.5 and a standard deviation of 0.5
])

for filename in os.listdir(DATA_DIR):
    if filename.endswith('.bytes') and filename not in processed_files: # look for files that end with .bytes and have not been processed
        filepath = os.path.join(DATA_DIR, filename)
        bytes_array = read_bytes(filepath)
        
        image_array = initial_size(bytes_array)
        visualize_data(image_array)
        
        image_array = handle_size(bytes_array, IMAGE_SIZE)
        visualize_data(image_array, True)
       
        
        # update log
        with open(PROCESSED_LOG, 'a') as f:
            f.write(filename + '\n')

print("Processing and saving images complete.")
