"""
A template for creating a AstroHub-compatible description of a model.

The places where you need to fill in information are marked with "TODO" comments
"""

# TODO: Import a metadata template appropriate for your type of model
#  See:
from metaData import AstroHubMetaData
from datacite import DataciteInfo
from model import BaseModel
import json


# Read in model from disk
AstroHubInfo = AstroHubMetaData()
dataciteInfo = DataciteInfo()
basemodel = BaseModel()

# Generate online build location for the model
AstroHubInfo.build_location()
# AstroHubInfo.set_files("Optional: model path")

# Define the name and title for the model
AstroHubInfo.set_title("A short title for the servable")
AstroHubInfo.set_name("AstroHub")
AstroHubInfo.set_publication_date()

# TODO: Verify authors and affiliations
dataciteInfo.set_creators("affiliations", "familyname", "givenname")

# TODO: Describe the scientific purpose of the model
AstroHubInfo.set_domains(["some", "pertinent", "fields"])

# TODO: Add references for the model
# dataciteInfo.set_identifier("10.IsDescribedBy","DOI")  # Example: Paper describing the model
dataciteInfo.set_datacite_description("description")
dataciteInfo.set_publicationYear("publicationYear")

# TODO: Describe the computational environment
# Basic route: Add a specific Python requirement
# AstroHubInfo.set_dependencies({"module_name":"version"})
# AstroHubInfo.set_version("version")
# AstroHubInfo.set_type()


# TODO: Describe the inputs and outputs of the model
#  This is not required for some model types (e.g., TensorFlow), delete if needed
basemodel.create_model()
basemodel.set_inputs('description', 'datatype:string',["shapeList"])
basemodel.set_method_details(False,"name","module")
basemodel.set_outputs('description', 'datatype:string',["shapeList"])
# basemodel.set_model_type("PyTorch")
# basemodel.set_parameters({"parameters":"parameters"})

res = {}
res.update({"datacite":dataciteInfo.datacite["datacite"], "AstroHub":AstroHubInfo.metadata["AstroHub"],
            "model":basemodel.modelInfo["model"]})

# Save the model info
with open('AstroHub_model.json', 'w') as fp:
    json.dump(res, fp, indent=2)