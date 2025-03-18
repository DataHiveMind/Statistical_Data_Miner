import torch
import torch.nn as nn
import torch.optim as optim

class PyTorchModel(nn.Module):
    def __init__(self, input_size):
        """
        Initializes a basic PyTorch model.
        
        Parameters:
        - input_size (int): Size of the input data.
        """
        super(PyTorchModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.output = nn.Linear(32, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.output(x)
        return x

# Example usage
if __name__ == "__main__":
    input_size = 10
    model = PyTorchModel(input_size)
    print(model)
