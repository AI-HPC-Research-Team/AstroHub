import os
import uuid
import time
import json

class BaseDataset:

    def __init__(self):
        self.metadata = {"AstroHub":{}}

    def set_uuid(self):
        uid = uuid.uuid1()
        if self.metadata.keys():
            self.metadata["AstroHub"].update({"id":str(uid)})
        return self.metadata

    def build_location(self):
        if self.metadata.keys():
            if "id" not in self.metadata["AstroHub"].keys():
                self.set_uuid()
            uid = self.metadata["AstroHub"]["id"]
            path = "/userhome/AstroHub/Dataset/"+ str(uid)
            self.metadata["AstroHub"].update({"build_location":path})
        return self.metadata


    # def set_domains(self,domains:list):
    #     if self.metadata.keys():
    #         self.metadata["AstroHub"].update({"domains":domains})
    #     return self.metadata

    def set_files(self,path=None):
        if path == None:
            path = "./"
        files = []
        for file in os.listdir(path):
            files.append(file)
        if self.metadata.keys():
            self.metadata["AstroHub"].update({"files":files})
        return self.metadata

    def set_name(self,name):
        if self.metadata.keys():
            self.metadata["AstroHub"].update({"name":name})
        return self.metadata

    def set_owner(self,owner):
        if self.metadata.keys():
            self.metadata["AstroHub"].update({"owner":owner})
        return self.metadata

    def set_publication_date(self):
        """
        data:format:y-m-d-h-m-s
        :param date:
        :return:
        """
        time_stamp = int(time.time()*1000)
        if self.metadata.keys():
            self.metadata["AstroHub"].update({"publication_date": time_stamp})
        return self.metadata

    def set_title(self,shorthandName):
        if self.metadata.keys():
            self.metadata["AstroHub"].update({"shorthand_name": shorthandName})
        return self.metadata

    def set_version(self,ver):
        if self.metadata.keys():
            self.metadata["AstroHub"].update({"version": ver})
        return self.metadata

    def set_type(self):
        if self.metadata.keys():
            self.metadata["AstroHub"].update({"type": "Dataset"})
        return self.metadata

    def related_model(self,uuid):
        if self.metadata.keys():
            self.metadata["AstroHub"].update({"related-model": uuid})
        return self.metadata

    # def set_if_visible(self):
    #     pass




