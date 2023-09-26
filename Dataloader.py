import torch
from torch.utils.data import DataLoader, random_split
from torchvision import transforms
from Dataset import MalwareDataset  

train_transform = transforms.Compose([
    transforms.ToTensor()
])

DATASET_DIR = 'E:\\University\\ZHON\\Dataset\\train_dir\\train_dir'  # path

dataset = MalwareDataset(DATASET_DIR, transform=train_transform)

# Split dataset into training and validation sets
train_size = int(0.8 * len(dataset))  # 80% of the dataset
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=50, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=50, shuffle=False)  

# Test DataLoader
#for images, labels in train_loader:
 #   print("Train Data:", images.shape, labels)
 #   break
#
#for images, labels in val_loader:
#    print("Validation Data:", images.shape, labels)
#   break
