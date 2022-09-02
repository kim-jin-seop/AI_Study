import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0, 5, 0.5, 0.5))
])

