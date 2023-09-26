import os
import shutil

def search_and_copy_files(src_dir, dest_dir, file_count, max_size_mb=1):
    """
    Search for .ocx files in src_dir and copy them to dest_dir until file_count is reached.
    Returns the number of files copied.
    """
    copied_count = 0
    max_size_bytes = max_size_mb * 1024 * 1024  # Convert MB to bytes
    
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.ocs'):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, file)
                
                # Check if the source and destination directories are the same
                if src_dir == dest_dir:
                    print("Source and destination directories are the same. Please provide a different destination directory.")
                    return
                
                # Check if source and destination file paths are the same
                if src_path == dest_path:
                    continue
                
                # Check the file size
                if os.path.getsize(src_path) > max_size_bytes:
                    continue
                
                # Check if the file already exists in the destination
                if os.path.exists(dest_path):
                    print(f"{file} already exists in the destination. Skipping.")
                    continue
                
                try:
                    # Copy the file to the destination directory
                    shutil.copy2(src_path, dest_path)
                    copied_count += 1
                except PermissionError:
                    print(f"Permission denied for {file}. Skipping.")
                
                # Check if we have reached the desired file_count
                if copied_count >= file_count:
                    return copied_count
    return copied_count

def main():
    # List of directories to search
    directories_to_search = [
        'C:\\Windows\\System32',
        'C:\\Windows\\SysWOW64',
        'C:\\Program Files',
        'C:\\Program Files (x86)',
        'C:\\Windows',
        'C:\\Users\\patri\\AppData',
        'C:\\Windows\\assembly',
        'C:\\Windows\\Microsoft.NET',
        'C:\\Users\\Public',
        'C:\\Users\\patri\\AppData\\Local',
        'C:\\Users\\patri\\AppData\\Roaming',
        'C:\\Users\\patri\\AppData\\LocalLow',
        'E:',
        'C:\\Windows\\winsxs',
        'C:\\Windows\\Installer',
        'C:\\Windows\\SoftwareDistribution\\Download',
        'C:\\ProgramData',
        'C:\\Users\\patri\\Documents',
        'C:\\Users\\patri\\Downloads',
        'C:\\Program Files\\Common Files',
        'C:\\Program Files (x86)\\Common Files',
        'C:\\Windows\\Temp',
        'C:\\Users\\patri\\AppData\\Local\\Temp',
        'C:\\Program Files\\Microsoft Office',
        'C:\\Program Files (x86)\\Microsoft Office'
    ]
    
    # Destination directory
    dest_directory = os.path.dirname(os.path.realpath(__file__))
    total_files_needed = 20000
    total_files_copied = 0

    for directory in directories_to_search:
        if total_files_copied < total_files_needed:
            total_files_copied += search_and_copy_files(directory, dest_directory, total_files_needed - total_files_copied)

    print(f"Copied {total_files_copied} files to {dest_directory}")

if __name__ == "__main__":
    main()
