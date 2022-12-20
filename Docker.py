import docker
import json
import os
import time

class DockerClient:
    """Main class for interacting with the Docker

    This class mainly used to help AstroHubClient compress files
    into docker image
    """

    def __init__(self, pcl_username):
        self.client = docker.from_env()
        self.usrname = pcl_username
        # super().__init__(pcl_username)



    def load_model(self,uuid):
        root = "/Users/renyiming/userhome/AstroHub/Models/"
        path = root + uuid
        for files in os.listdir(path):
            print(path+files)
        return path


    def load_data(self,uuid):
        root = "/Users/renyiming/userhome/AstroHub/Dataset/"
        path = root + uuid
        for files in os.listdir(path):
            print(path + files)
        return path

    def get_dependencies(self,uuid):
        """Get model dependencies by parsing json

        """
        model_json = "/Users/renyiming/userhome/AstroHub/Models/models.json"
        model_instance = json.load(open(model_json))
        if uuid:
            # model_info = model_instance[0]
            res = []
            for i in model_instance:
                if i['AstroHub']['id'] == uuid:
                    res.append(i['AstroHub']['dependencies'])
            if len(res) == 0:
                return "No match results~"
            else:
                return res
        else:
            raise ValueError(
                "Search function requires at least one parameter"
            )

    def get_requirements(self,uuid):
        """Make requirements file

        :param uuid:
        :return:
        """
        model_instance = self.get_dependencies(uuid)
        dependencies = model_instance[0]
        requirement = open("/Users/renyiming/userhome/AstroHub/requirements.txt", 'w')
        for key, value in dependencies.items():
            if key == 'torch' or key == 'torchvision':
                continue
            requirement.write(str(key) + '==' + str(value) + '\n')
        print('Requirements Done')
        requirement.close()

    def docker_file(self,model_id,data_id):
        """Make Docker file

        :param model_id:
        :param data_id:
        :return:
        """
        dockerfile = open("/Users/renyiming/userhome/AstroHub/Dockerfile", 'w')
        # self.get_requirements(model_id)
        doc = ['FROM python:3.7'+'\n','MAINTAINER '+self.usrname+'\n','RUN mkdir /src','WORKDIR /src'+'\n',
               'COPY requirements.txt /src/requirements.txt',
               "RUN pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/" + '\n',
               'COPY ./Models/'+model_id +" /src",
               'COPY ./Dataset/'+data_id +" /src",
               'COPY ./env  /src',
               'RUN pip install IPython -i https://pypi.mirrors.ustc.edu.cn/simple/'+'\n',
               "EXPOSE 10001"+'\n']
        for i in doc:
            dockerfile.write(i + '\n')
        print('Dockerfile Done')
        dockerfile.close()


#     def list_image(self):
#         return self.client.images.list()


    def build_image(self,model_id):
        """Make Docker image

        :param model_id:
        :return:
        """
        root = "/Users/renyiming/userhome/AstroHub/"
        os.system('docker build -t astrohub:' + model_id +' ' + root)

        return 0


    def delete_image(self,image,force):
        return self.client.images.remove(image=image,force=force)

    # def list_containers(self):
    #     return self.client.containers.list(all=True)

    # def prune_containers(self):
    #     return self.client.containers.prune()

