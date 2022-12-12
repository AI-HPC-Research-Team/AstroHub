import json

class BaseModel:

    def __init__(self):
        self.modelInfo = {}


    def create_model(self):
        self.modelInfo.update({"model":{"methods":{"run":{}},"type":""}})
        return self.modelInfo


    def set_inputs(self,description,data_type,shape=None):
        if self.modelInfo.keys():
            input =self.modelInfo["model"]["methods"]["run"]
            if shape == None:
                input.update({"input":{"description":description, "type":data_type}})
            else:
                input.update({"input": {"description": description, "shape": shape,
                                        "type": data_type}})
        return self.modelInfo


    def set_method_details(self,batch,name,module):
        if self.modelInfo.keys():
            input = self.modelInfo["model"]["methods"]["run"]
            input.update({"method_details": {"autobatch": batch, "method_name": name,
                                    "module": module}})
        return self.modelInfo


    def set_outputs(self,description,data_type,shape=None):
        if self.modelInfo.keys():
            output = self.modelInfo["model"]["methods"]["run"]
            if shape == None:
                output.update({"output":{"description":description,"type":data_type}})
            else:
                output.update({"output": {"description": description, "shape": shape,
                                        "type": data_type}})
        return self.modelInfo


    def set_model_type(self,modelType):
        if self.modelInfo.keys():
            self.modelInfo["model"]["type"] = modelType
        return self.modelInfo


    def set_parameters(self,parameters = None):
        if self.modelInfo.keys():
            if parameters == None:
                return self.modelInfo
            else:
                parameter = self.modelInfo["model"]["methods"]["run"]
                parameter.update({"parameters":parameters})
        return self.modelInfo

