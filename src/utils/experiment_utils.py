import random
import argparse
from pathlib import Path

import numpy as np
import torch
import yaml


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42, 
                        help="Set a seed to enable experiment reproducibility.")
    parser.add_argument("--experiment_name", type=str, required=True, 
                        help="Specify the experiment name to load the config and save the artifacts.")
    
    pass # Add further arguments to the parser here

    return parser.parse_args()


def set_seeds(seed):
    random.seed(seed)
    np.random.seed(seed)
    # Set the seed for PyTorch on the CPU
    torch.manual_seed(seed)
    # Set the seed for all available GPUs
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_config(experiment_path):
    try:
        with open(experiment_path / "config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")
    
    return config
