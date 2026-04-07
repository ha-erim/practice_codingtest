from torchvision import datasets, transforms
import torch
from torch.utils.data import DataLoader
from torch import nn

# 1. 데이터
transform = transforms.Compose([transforms.ToTensor()])

train_dataset = datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)
test_dataset = datasets.MNIST(
    root="./data", train=False, download=True, transform=transform
)

train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=32, shuffle=False)


# 2. 모델
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(
            in_channels=16, out_channels=32, kernel_size=3, padding=1
        )
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, img):
        out = self.conv1(img)  # [B, 16, 28, 28]
        out = self.relu(out)
        out = self.pool(out)  # [B, 16, 14, 14]

        out = self.conv2(out)  # [B, 32, 14, 14]
        out = self.relu(out)
        out = self.pool(out)  # [B, 32, 7, 7]

        out = out.view(out.size(0), -1)  # [B, 32*7*7]
        out = self.fc1(out)
        out = self.relu(out)
        out = self.fc2(out)  # [B, 10]
        return out


model = CNN()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)


# 3. 학습
def train(epochs):
    model.train()
    for epoch in range(epochs):
        total_loss = 0.0

        for img, label in train_dataloader:
            optimizer.zero_grad()
            outputs = model(img)
            loss = criterion(outputs, label)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(train_dataloader)
        print(f"{epoch+1} epoch, loss: {avg_loss:.4f}")


# 4. 평가
def test():
    model.eval()
    correct = 0

    with torch.no_grad():
        for img, label in test_dataloader:
            outputs = model(img)
            preds = torch.argmax(outputs, dim=1)
            correct += (preds == label).sum().item()

    acc = correct / len(test_dataset)
    print(f"Test Accuracy: {acc:.4f}")


train(5)
test()
