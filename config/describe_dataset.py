"""
A template for creating a AstroHub-compatible description of a dataset.

The places where you need to fill in information are marked with "TODO" comments
"""

# TODO: Import a metadata template appropriate for your type of dataset
#  See:
from dataset import BaseDataset
import json


# Read in dataset from disk
dataset = BaseDataset()


# Generate online build location for the dataset
dataset.build_location()
# AstroHubInfo.set_files("Optional: dataset path")

# Define the basic info for the dataset
dataset.set_title("A short title for the dataset")
dataset.set_name("AstroHub")
dataset.set_owner("owner")
dataset.set_publication_date()
dataset.set_version("version")
dataset.set_type()


# Define the related model based on model_id for the dataset
dataset.related_model("d400a239-c252-4fec-bf17-a9ded50729ba")


res = {}
res.update({"AstroHub":dataset.metadata["AstroHub"]})

# Save the dataset info
with open('AstroHub_dataset.json', 'w') as fp:
    json.dump(res, fp, indent=2)