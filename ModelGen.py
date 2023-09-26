import torch.nn as nn
from Dataloader import train_loader  # testing


class MalwareClassifierCNN(nn.Module):
    def __init__(self, num_classes=10):
        super(MalwareClassifierCNN, self).__init__()
        
        self.conv_layers = nn.Sequential(

            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)  
        )
        
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 28 * 28, 64),  
            nn.ReLU(),
            nn.Linear(64, num_classes),  
            nn.Softmax(dim=1)  
        )
        
    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x

# Instantiate the model
model = MalwareClassifierCNN(num_classes=2)  
print(model)

#testing functionality
#dataiter = iter(train_loader)
#images, labels = next(dataiter)

# Pass data through the model
#outputs = model(images)

# Check output shape
#print("Output shape:", outputs.shape)
