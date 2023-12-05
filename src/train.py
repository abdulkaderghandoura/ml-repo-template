import random
import argparse
from pathlib import Path
import numpy as np
import torch
import yaml


def set_seeds(seed):
    random.seed(seed)
    np.random.seed(seed)
    # Set the seed for PyTorch on the CPU
    torch.manual_seed(seed)
    # Set the seed for all available GPUs
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def main(args):
    set_seeds(args.seed)
    
    try:
        experiment_path = Path("..") / "experiments" / f"experiment_{args.experiment_num}"
        with open(experiment_path / "config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")
    
    # Train code here..


def get_args():
    parser = argparse.ArgumentParser(description="Training Script")
    parser.add_argument("--seed", type=int, default=42, 
                        help="Set a seed to enable experiment reproducibility.")
    parser.add_argument("--experiment_num", type=int, required=True, 
                        help="Specify the experiment number to load configs and save artifacts.")
    
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    main(args)