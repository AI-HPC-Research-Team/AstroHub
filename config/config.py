import os

class AstroHubEnv:
    """Main class for initializing remote env, includes
    node and k8s, docker config

    """

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
        """Generate model describing file for users

        :param path:
        :return:
        """
        os.system("cp ./describe_model.py " + path)
        return

    def describe_data(self,path):
        """Generate data describing file for users

        :param path:
        :return:
        """
        os.system("cp ./describe_dataset.py " + path)
        return
