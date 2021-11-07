# AstroHub
An AI hub for astronomy and astrophysics. The platform, based on PCL Cloud Brain, provides a remote library for the pre-training model and dataset. It lets users complete the retraining and inference processes by executing a simple API locally.
## Structure
AstroHub, developed based on PCL Cloud Brain, mainly includes three modules, publish, search, and run. The Publish module accesses the remote computing node through the SSH command to complete the upload process of model and data pipeline. It then saves the corresponding information into JSON. The Search module can filter name, owner, domain to obtain the corresponding model/data list by parsing the JSON on the storage node. The Run module is based on the Kubernetes and Docker framework, allowing remote computing nodes to distributed execute the selected model and dataset.


<img src="Structure.jpg" width="700" height="700"/><br/>
## Installation
### Environment
AstroHub operating environment is composed of Master node and Slave nodes. The physical machine requires to be configured with Kubernetes and Docker environment. Configuration instruction refers to [Kubernetes](https://kubernetes.io/docs/setup/), [Docker](https://docs.docker.com/get-started/overview/).
## Example Usage

The following sections are short introductions to using the AstroHub.

### Discovering and Running Models

#### Search the Model/Dataset
#### Run Models

### Publishing a Model/Dataset

As a simple example, we will show how to submit a machine learning model created based on the Mnist.
Full scripts for this example model are in examples.

#### Describe the Model
#### Describe the Dataset



## Project Support
This material is based upon work supported by PengCheng Lab.
