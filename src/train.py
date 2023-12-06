from pathlib import Path

import numpy as np
import torch

from utils.experiment_utils import get_args, set_seeds, load_config
# Modify according to your model and dataset modules
from models.model_name import YourModel
from datasets.custom_dataset_name import CustomDataset


def main(args):
    dataset_path = Path("..") / "data" / "dataset_name"
    experiment_path = Path("..") / "experiments" / args.experiment_name

    set_seeds(args.seed)
    config = load_config(experiment_path)
    
    pass  # Train code here..


if __name__ == "__main__":
    parsed_args = get_args()
    main(parsed_args)
