
from datasets import load_dataset
import os
import pandas as pd 

# https://huggingface.co/datasets/knkarthick/dialogsum
huggingface_dataset_name = "knkarthick/dialogsum"

dataset = load_dataset(huggingface_dataset_name)

train = dataset['train']

output_folder = "output"
os.makedirs(os.path.dirname(f"./{output_folder}/"), exist_ok=True)
train.to_csv(f"{output_folder}/dialogsum_train.csv", index=False)

test = dataset['test']
test.to_csv(f"{output_folder}/dialogsum_test.csv", index=False)

validation = dataset['validation']
validation.to_csv(f"{output_folder}/dialogsum_validation.csv", index=False)
