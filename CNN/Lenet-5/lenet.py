import torch
import torch.nn as nn
import torch.nn.functional as F


class LeNet(nn.Module):
    def __init__(self):
        super().__init__()
        # input size = ?*32*32*1
        # conv1 = ?*28*28@6
        # pool = ?*14*14@6
        # conv2 = ?*10*10@16
        # pool = ?*5*5@16
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, stride=1),
            nn.ReLU()
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1),
            nn.ReLU()
        )
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        self.fc1 = nn.Sequential(
            nn.Linear(in_features=5 * 5 * 16, out_features=120),
            nn.ReLU()
        )
        self.fc2 = nn.Sequential(
            nn.Linear(in_features=120, out_features=84),
            nn.ReLU()
        )
        self.fc3 = nn.Sequential(
            nn.Linear(in_features=84, out_features=10),
            nn.Softmax()  # LogSoftmax
        )

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.pool(x)  # ?*5*5*16
        x = x.view(-1, 5 * 5 * 16)  # ?*400
        x = self.fc1(x)
        x = self.fc2(x)
        out = self.fc3(x)
        return out
