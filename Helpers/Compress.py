import os
import zipfile

# Constants
SOURCE_DIR = 'E:\\University\\ZHON\dllspys\\Greyscales'  # from
TARGET_ZIP = 'E:\\University\\ZHON\\testBenign_GS.zip'  # Path to the target zip file
PROCESSED_LOG = 'processed_files.txt'  # keep track of processed files
FILE_LIMIT = 10868  # Number of files to process

def compress_files(source_dir, target_zip, file_limit):
    # Check if a log file exists, and if so, get the list of processed files
    processed_files = set()
    if os.path.exists(PROCESSED_LOG):
        with open(PROCESSED_LOG, 'r') as f:
            processed_files = set(f.read().splitlines())

    # Get the list of .png files from the source directory
    all_files = [f for f in os.listdir(source_dir) if f.endswith('.png') and f not in processed_files]
    files_to_process = all_files[:file_limit]

    # Compress the selected files
    with zipfile.ZipFile(target_zip, 'a') as zipf:
        for file in files_to_process:
            zipf.write(os.path.join(source_dir, file), file)
            # Log the processed file
            with open(PROCESSED_LOG, 'a') as f:
                f.write(file + '\n')

    print(f"Compressed {len(files_to_process)} files to {target_zip}.")

if __name__ == '__main__':
    compress_files(SOURCE_DIR, TARGET_ZIP, FILE_LIMIT)
