import torch
from torch import nn
import torch.nn.functional as F
 
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = nn.Linear(5,5)
 
    def forward(self,x):
        net = self.lin1(x)
        return net
 
device = torch.device("mps") if torch.backends.mps.is_available() else "cpu"
print(f"device: {device}")
 
# MPS 장치에 바로 tensor를 생성합니다.
x = torch.ones(5, device=device)