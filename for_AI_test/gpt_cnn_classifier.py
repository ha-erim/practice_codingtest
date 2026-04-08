import torch
from torch import nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. 데이터
transform = transforms.Compose([transforms.ToTensor()])

train_dataset = datasets.MNIST(
    root="./data", train=True, download=False, transform=transform
)
test_dataset = datasets.MNIST(
    root="./data", train=False, download=False, transform=transform
)

batchsize = 32

train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=batchsize)
test_dataloader = DataLoader(test_dataset, shuffle=False, batch_size=batchsize)


class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, 1)
        self.conv2 = nn.Conv2d(16, 32, 3, 1)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)
        self.fc = nn.Linear(32 * 24 * 24, 10)

    def forward(self, x):
        out1 = self.conv1(x)
        out1 = self.relu(out1)
        out1 = self.dropout(out1)

        out2 = self.conv2(out1)
        out2 = self.relu(out2)
        out2 = self.dropout(out2)

        out3 = out2.view(out2.size(0), -1)
        out3 = self.fc(out3)
        return out3


# device = "mps" if torch.backends.mps.is_available() else "cpu"
device = "cpu"
model = CNN().to(device)
lr = 1e-3
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)


def train(epochs):
    model.train()
    print(f"device : {device}")
    for epoch in range(epochs):
        total_loss = 0.0

        for img, label in train_dataloader:
            img, label = img.to(device), label.to(device)

            optimizer.zero_grad()
            output = model(img)
            loss = criterion(output, label)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(train_dataloader)
        print(f"[{epoch+1} epoch] loss: {avg_loss:.4f}")


# def test():
#     model.eval()
#     with torch.no_grad():
#         correct = 0
#         for img, label in test_dataloader:
#             img, label = img.to(device), label.to(device)
#             output = model(img)
#             pred = torch.argmax(output, dim=1)
#             correct += (pred == label).sum().item()
#     acc = correct / len(test_dataset)

#     print(f"acc : {acc}")


def test():
    model.eval()
    with torch.no_grad():
        correct = 0
        total_loss = 0.0

        for img, label in test_dataloader:
            img, label = img.to(device), label.to(device)

            output = model(img)

            # ✅ loss 추가
            loss = criterion(output, label)
            total_loss += loss.item()

            pred = torch.argmax(output, dim=1)
            correct += (pred == label).sum().item()

    acc = correct / len(test_dataset)
    avg_loss = total_loss / len(test_dataloader)

    print(f"test loss: {avg_loss:.4f}, acc: {acc:.4f}")


train(10)
test()
