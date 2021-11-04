# from .client import DLHubClient  # noqa F401 (import unused)
# from .version import __version__  # noqa F401 (import unused)
import json
import test_json
import os,sys
import uuid
# print(uuid.uuid1())
# dic = [{'datacite': {'alternateIdentifiers': [], 'creators': [], 'descriptions': [], 'fundingReferences': [], 'identifier': {'identifier': '10.YET/UNASSIGNED', 'identifierType': 'DOI'}, 'publicationYear': '2020', 'publisher': 'DLHub', 'relatedIdentifiers': [{'relatedIdentifier': 'globus:DK68RMRsIurZ', 'relatedIdentifierType': 'Globus', 'relationType': 'IsDescribedBy'}], 'resourceType': {'resourceTypeGeneral': 'InteractiveResource'}, 'rightsList': [], 'titles': [{'title': 'Norm of a 1D Array'}]}, 'dlhub': {'build_location': '/mnt/dlhub_ingest/a267fced-370f-4f2d-9567-1fc11c9b3ba1-1598379008', 'domains': [], 'ecr_arn': 'arn:aws:ecr:us-east-1:039706667969:repository/a267fced-370f-4f2d-9567-1fc11c9b3ba1', 'ecr_uri': '039706667969.dkr.ecr.us-east-1.amazonaws.com/a267fced-370f-4f2d-9567-1fc11c9b3ba1', 'files': {}, 'funcx_id': 'effddfa5-f597-49a1-b48b-21684e2374ca', 'id': 'a267fced-370f-4f2d-9567-1fc11c9b3ba1', 'identifier': 'globus:DK68RMRsIurZ', 'name': '1d_norm', 'owner': 'dlhub.test_gmail', 'publication_date': '1598379008081', 'shorthand_name': 'dlhub.test_gmail/1d_norm', 'test': False, 'transfer_method': {'POST': 'file', 'path': '/mnt/tmp/servable.zip'}, 'type': 'servable', 'user_id': '4', 'version': '0.9.0', 'visible_to': ['public']}, 'servable': {'methods': {'run': {'input': {'description': 'Array to be normed', 'shape': ['None'], 'type': 'ndarray'}, 'method_details': {'autobatch': False, 'method_name': 'norm', 'module': 'numpy.linalg'}, 'output': {'description': 'Norm of the array', 'type': 'number'}, 'parameters': {}}}, 'shim': 'python.PythonStaticMethodServable', 'type': 'Python static method'}}, {'datacite': {'alternateIdentifiers': [], 'contributors': [], 'creators': [], 'descriptions': [], 'fundingReferences': [], 'identifier': {'identifier': '10.datacite/placeholder', 'identifierType': 'DOI'}, 'publicationYear': '', 'publisher': 'DLHub', 'relatedIdentifiers': [], 'resourceType': {'resourceTypeGeneral': 'InteractiveResource'}, 'rightsList': [], 'subjects': [], 'titles': [{'title': 'Norm of a 1D Array'}]}, 'dlhub': {'build_location': '/mnt/dlhub_ingest/056988f0-24d3-4490-8620-de1a6cf4f16a-1631897495', 'dependencies': {}, 'domains': [], 'ecr_arn': 'arn:aws:ecr:us-east-1:039706667969:repository/056988f0-24d3-4490-8620-de1a6cf4f16a', 'ecr_uri': '039706667969.dkr.ecr.us-east-1.amazonaws.com/056988f0-24d3-4490-8620-de1a6cf4f16a', 'files': {}, 'funcx_id': 'bb99fcbb-42e1-4450-97b4-14942e63e47a', 'id': '056988f0-24d3-4490-8620-de1a6cf4f16a', 'name': '1d_norm', 'owner': 'None', 'publication_date': '1631897404890', 'shorthand_name': 'None/1d_norm', 'test': True, 'transfer_method': {'POST': 'file', 'path': '/mnt/tmp/servable.zip'}, 'type': 'servable', 'user_id': 'None', 'version': '0.9.6', 'visible_to': ['public']}, 'servable': {'methods': {'run': {'input': {'description': 'Array to be normed', 'shape': ['None'], 'type': 'ndarray'}, 'method_details': {'autobatch': False, 'method_name': 'norm', 'module': 'numpy.linalg'}, 'output': {'description': 'Norm of the array', 'type': 'number'}, 'parameters': {}}}, 'options': {}, 'shim': 'python.PythonStaticMethodServable', 'type': 'Python static method'}}, {'datacite': {'alternateIdentifiers': [], 'contributors': [], 'creators': [], 'descriptions': [], 'fundingReferences': [], 'identifier': {'identifier': '10.datacite/placeholder', 'identifierType': 'DOI'}, 'publicationYear': '', 'publisher': 'DLHub', 'relatedIdentifiers': [], 'resourceType': {'resourceTypeGeneral': 'InteractiveResource'}, 'rightsList': [], 'subjects': [], 'titles': [{'title': 'Norm of a 1D Array'}]}, 'dlhub': {'build_location': '/mnt/dlhub_ingest/945360f7-d24f-4586-8835-218132734d34-1631900116', 'dependencies': {}, 'domains': [], 'ecr_arn': 'arn:aws:ecr:us-east-1:039706667969:repository/945360f7-d24f-4586-8835-218132734d34', 'ecr_uri': '039706667969.dkr.ecr.us-east-1.amazonaws.com/945360f7-d24f-4586-8835-218132734d34', 'files': {}, 'funcx_id': '13b6346c-6a55-4cea-8331-67a0d79b7b94', 'id': '945360f7-d24f-4586-8835-218132734d34', 'name': '1d_norm', 'owner': '1a90406d-63d0-4aa7-8026-1ac2dbc3f4cd_clients', 'publication_date': '1631900075076', 'shorthand_name': '1a90406d-63d0-4aa7-8026-1ac2dbc3f4cd_clients/1d_norm', 'test': True, 'transfer_method': {'POST': 'file', 'path': '/mnt/tmp/servable.zip'}, 'type': 'servable', 'user_id': '37', 'version': '0.9.6', 'visible_to': ['public']}, 'servable': {'methods': {'run': {'input': {'description': 'Array to be normed', 'shape': ['None'], 'type': 'ndarray'}, 'method_details': {'autobatch': False, 'method_name': 'norm', 'module': 'numpy.linalg'}, 'output': {'description': 'Norm of the array', 'type': 'number'}, 'parameters': {}}}, 'options': {}, 'shim': 'python.PythonStaticMethodServable', 'type': 'Python static method'}}]

# print(json.dumps(dic,indent=1))
# project_path = os.path.dirname(os.path.abspath(__file__))
# print(project_path)
# # with open('/Users/renyiming/PycharmProjects/AstroHub/test_json/search_res_result1.json','w') as fp:
# #     print(json.dump(dic,fp,indent=1))
#
path = "/Users/renyiming/userhome/AstroHub/Models/"
for dirs in os.listdir(path):
    # for dir in dirs:
    #     # 获取目录的名称
    #     print(dir)
    #     # 获取目录的路径
    #     print(os.path.join(root, dir))
    print(path+dirs)
#
#
# a = {'111':{'111':1}}
# print(a)

# import docker
# client = docker.from_env()
# print(client.images.build())

