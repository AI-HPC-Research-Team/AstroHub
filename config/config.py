import os

class AstroHubEnv:

    def __init__(self):
        pass
    #
    # def kubernetes_config(self):
    #     pass
    #
    # def docker_config(self):
    #     pass

    # def communication(self,path):
    #     pass

    def initisalize_env(self):
        """
        initialize basic dir for models, dataset and env
        :return:
        """
        pass

    def describe_model(self,path):
        os.system("cp ./describe_model.py " + path)
        return

    def describe_data(self,path):
        os.system("cp ./describe_dataset.py " + path)
        return
