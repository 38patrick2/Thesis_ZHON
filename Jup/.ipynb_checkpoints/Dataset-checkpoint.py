import os
import torch
import pathlib
from PIL import Image
from torch.utils.data import Dataset
from typing import List, Dict, Tuple

def find_classes(directory: str) -> Tuple[List[str], Dict[str, int]]:
    """Finds the class folder names in a target directory.
    
    Args:
        directory (str): target directory to load classnames from.

    Returns:
        Tuple[List[str], Dict[str, int]]: (list_of_class_names, dict(class_name: idx...))
    """
    classes = sorted(entry.name for entry in os.scandir(directory) if entry.is_dir())
    if not classes:
        raise FileNotFoundError(f"Couldn't find any classes in {directory}.")
    class_to_idx = {cls_name: i for i, cls_name in enumerate(classes)}
    return classes, class_to_idx

class MalwareDataset(Dataset):
    """Custom dataset for malware images."""
    
    def __init__(self, targ_dir: str, transform=None) -> None:
        """Initialize the dataset with target directory and optional transforms."""
        
        # Collect and sort all image paths from the target directory
        self.image_paths = sorted(list(pathlib.Path(targ_dir).glob("*/*.png")))
        
        self.transform = transform
        self.classes, self.class_to_idx = find_classes(targ_dir)

    def __len__(self) -> int:
        """Return the total number of samples."""
        return len(self.image_paths)
    
    def __getitem__(self, index: int) -> Tuple[torch.Tensor, int]:
        """Return one sample of data, data and label (X, y)."""
        img_path = self.image_paths[index]
        img = Image.open(img_path)
        
        class_name = img_path.parent.name  # Extract class name from the path
        class_idx = self.class_to_idx[class_name]
        
        if self.transform:
            img = self.transform(img)
        
        return img, class_idx
