import torch
from Dataset import MalwareDataset


DATASET_DIR = 'E:\\University\\ZHON\\Dataset\\train_dir\\train_dir'  


dataset = MalwareDataset(DATASET_DIR)

print(f"Total number of samples in the dataset: {len(dataset)}")

sample_img, sample_label = dataset[0]  
print(f"Shape of the sample image: {sample_img.shape}")
print(f"Label of the sample image: {sample_label}")

import matplotlib.pyplot as plt
plt.imshow(sample_img.permute(1, 2, 0))
plt.title(f"Class: {sample_label}")
plt.show()
