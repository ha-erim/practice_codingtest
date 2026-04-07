from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader


# 1. 데이터 생성
X, y = make_classification(
    n_samples=1200,
    n_features=20,
    n_informative=12,
    n_redundant=4,
    n_classes=3,
    random_state=42,
)

# 2. train / test 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. 정규화
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. torch tensor로 변환
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)

# 5. dataset / dataloader
train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)

train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=32, shuffle=False)


# 6. 모델 정의
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(20, 40)
        self.layer2 = nn.Linear(40, 3)
        self.layer3 = nn.Linear(60, 3)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.2)

    def forward(self, X):
        out = self.layer1(X)
        out = self.relu(out)
        out = self.dropout(out)

        out = self.layer2(out)
        # out = self.relu(out)
        # out = self.dropout(out)

        # out = self.layer3(out)
        return out


# 7. 모델, loss, optimizer 생성
model = Net()
criterion = nn.CrossEntropyLoss()
# optimizer = torch.optim.SGD(model.parameters(), lr=1e-2)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-2)


# 8. 학습 함수
def training_loop(epochs):
    model.train()

    for epoch in range(epochs):
        total_loss = 0.0

        for X_batch, y_batch in train_dataloader:
            optimizer.zero_grad()

            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)

            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(train_dataloader)
        print(f"Epoch [{epoch+1}/{epochs}] Loss: {avg_loss:.4f}")


# 9. 평가 함수
def test_loop():
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for X_batch, y_batch in test_dataloader:
            outputs = model(X_batch)
            preds = torch.argmax(outputs, dim=1)

            correct += (preds == y_batch).sum().item()
            total += y_batch.size(0)

    accuracy = correct / total
    print(f"Test Accuracy: {accuracy:.4f}")


# 10. 실행
training_loop(50)
test_loop()
