import torch
from torch.utils.data import DataLoader, random_split
from torchvision import transforms
from Dataset import MalwareDataset  # Only import MalwareDataset

train_transform = transforms.Compose([
    transforms.ToTensor()
])

DATASET_DIR = '/home/vboxuser/Work/ZHON/Dataset/train_dir'  # Replace with the path to your dataset

# Create an instance of the MalwareDataset
dataset = MalwareDataset(DATASET_DIR, transform=train_transform)

# Split the dataset into training and validation sets
train_size = int(0.8 * len(dataset))  # 80% of the dataset
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=50, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=50, shuffle=False)  # No need to shuffle validation data

# Test the DataLoader
#for images, labels in train_loader:
#    print("Train Data:", images.shape, labels)
#    break
#
#for images, labels in val_loader:
#    print("Validation Data:", images.shape, labels)
#    break
