import tensorflow as tf
import torch

def evaluate_tensorflow_model(model, x_test, y_test):
    """
    Evaluates the TensorFlow model.
    """
    results = model.evaluate(x_test, y_test, verbose=1)
    print(f"Test Loss: {results[0]}, Test MAE: {results[1]}")

def evaluate_pytorch_model(model, dataset):
    """
    Evaluates the PyTorch model.
    """
    data_loader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=False)
    model.eval()
    total_loss = 0
    criterion = torch.nn.MSELoss()
    
    with torch.no_grad():
        for batch in data_loader:
            x, y = batch
            predictions = model(x)
            loss = criterion(predictions, y)
            total_loss += loss.item()
    print(f"Test Loss: {total_loss / len(data_loader)}")
