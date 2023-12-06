import torch
import torch.nn as nn


class YourModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(YourModel, self).__init__()
        self.input_size = input_size
        self.output_size = output_size
        pass  # Define layers and parameters here

    def forward(self, x):
        pass  # Define the forward pass

        return x
