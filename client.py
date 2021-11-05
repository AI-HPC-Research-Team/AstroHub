import logging
import json
import os
import time
from warnings import warn
import pandas as pd
from Docker import DockerClient
from Kubernetes.Kubernetes import KubernetClient
from tabulate import tabulate
import click
from kubernetes import client
import docker


import requests



class AstroHubClient(KubernetClient,DockerClient):

    def __init__(self, pcl_username, pcl_password):
        super().__init__()
        self.client = docker.from_env()
        self.core = client.CoreV1Api()
        self.batch = client.BatchV1Api()
        header = {"content-length": "64", "content-Type": "application/json; charset=utf-8", "host": "192.168.204.24"}
        # body = {"username":pcl_username, "password": pcl_password, "expiration": 604800}
        body = {"username": "renym", "password": "renym@2021", "expiration": 604800}
        url = 'http://192.168.204.24/rest-server/api/v1/token'
        response = requests.post(url, json=body, headers=header)
        res = json.loads(response.text)
        if res['msg'] == 'success':
            ash_authorizer = res['payload']['token']
            usrname = res['payload']['username']
            self.authorizer = ash_authorizer
            self.usrname = usrname
        else:
            raise ValueError(
                "AstroHub can only take authorizers from PCL account, but you have provided other format"
            )


    @property
    def get_instance(self):
        # model_json = "/Users/renyiming/userhome/AstroHub/Models/search_result.json"
        # data_json = "/Users/renyiming/userhome/AstroHub/Dataset/search_result.json"
        model_json = "/Users/renyiming/userhome/AstroHub/Models/models.json"
        data_json = "/Users/renyiming/userhome/AstroHub/Dataset/dataset.json"
        model_instance = json.load(open(model_json))
        data_instance = json.load(open(data_json))

        # env_dir = os.listdir(r"/Users/renyiming/userhome/AstroHub/env")
        return model_instance,data_instance

    # def publish(self,path):
    #     pass

    def filter_latest(self,res):
        res_dic = {}
        for i in res:
            if 'publication_date' not in i['AstroHub']:
                warn(
                    'Found entries in AstroHub index that lack publication_date.'
                    ' Please contact AstroHub team',RuntimeWarning
                )
                continue
            if 'name' not in i['AstroHub']:
                warn(
                    'Found entries in AstroHub index that lack name.'
                    ' Please contact AstroHub team', RuntimeWarning
                )
                continue
            uuid = i['AstroHub']['name'] + '_' + i['AstroHub']['owner']
            publication_date = int(i['AstroHub']['publication_date'])
            if uuid not in res_dic.keys():
                res_dic.update({uuid:i})
            else:
                if int(res_dic[uuid]['AstroHub']['publication_date']) < publication_date:
                    res_dic[uuid] = i
        return [[i['AstroHub']['id'],i['AstroHub']['owner'],i['AstroHub']['name'],
                 time.strftime("%Y-%m-%d %H:%M", time.localtime(int(i['AstroHub']['publication_date'])/1000)),
                 i['model']['type'],i['AstroHub']['dependencies']] for i in res_dic.values()]

    def search_all_model(self):
        model_info = self.get_instance[0]
        model_lis = set()
        for i in model_info:
            model_lis.add(i['AstroHub']['shorthand_name'])
        return list(model_lis)

    def modelSearch_id(self,uuid):
        if uuid:
            model_info = self.get_instance[0]
            res = []
            for i in model_info:
                # print(i)
                print(i['AstroHub']['id'])
                if i['AstroHub']['id'] == uuid:
                    res.append(i)
            if len(res) == 0:
                return "No match results~"
            else:
                return self.filter_latest(res)
        else:
            raise ValueError(
                "Search function requires at least one parameter"
            )

    def modelSearch_name(self,name):
        if name:
            model_info = self.get_instance[0]
            res = []
            for i in model_info:
                if i['AstroHub']['name'] == name:
                    res.append(i)
            if len(res) == 0:
                return "No match results~"
            else:
                return self.filter_latest(res)
        else:
            raise ValueError(
                "Search function requires at least one parameter"
            )

    def modelSearch_author(self,author):
        if author:
            model_info = self.get_instance[0]
            res = []
            creator = author.split(',')
            familyName = creator[0]
            givenName = creator[1]
            for i in model_info:
                if 'creators' in i['datacite'] and \
                        len(i['datacite']['creators'])>0 and \
                        i['datacite']['creators'][0]['familyName'] == familyName and \
                        i['datacite']['creators'][0]['givenName'] == givenName:
                    res.append(i)
            if len(res) == 0:
                return "No match results~"
            else:
                return self.filter_latest(res)
        else:
            raise ValueError(
                "Search function requires at least one parameter"
            )


    def modelSearch_domains(self,domain):
        if domain:
            model_info = self.get_instance[0]
            res = []
            for i in model_info:
                if 'domains' in i['AstroHub'] and \
                        len(i['AstroHub']['domains'])>0 and \
                        domain in i['AstroHub']['domains']:
                    res.append(i)
            if len(res) == 0:
                return "No match results~"
            else:
                result = self.filter_latest(res)
                return self.parsing_result(result,10)
        else:
            raise ValueError(
                "Search function requires at least one parameter"
            )


    def modelSearch_related_doi(self,doi):
        if doi:
            model_info = self.get_instance[0]
            res = []
            for i in model_info:
                if 'identifier' in i['datacite']['identifier'] and \
                        i['datacite']['identifier']['identifier'] == doi:
                    res.append(i)
            if len(res) == 0:
                return "No match results~"
            else:
                result = self.filter_latest(res)
                return self.parsing_result(result,10)
        else:
            raise ValueError(
                "Search function requires at least one parameter"
            )

    def parsing_result(self,res,limit):
        if len(res) > limit:
            enum = limit
        else:
            enum = len(res)
        results_rf = pd.DataFrame([{
            'uuid':res[i][0],
            'Owner': res[i][1],
            'Model Name': res[i][2],
            'Publication Date': res[i][3],
            'Type': res[i][4]
            } for i in range(enum)])
        # results_rf.sort_values(['Owner', 'Model Name', 'Publication Date'],
        #                        ascending=[True, True, False], inplace=True)
        return results_rf

    # def common_options(f):
    #     """
    #     Global/shared options decorator.
    #
    #     :param f:
    #     :return:
    #     """
    #     f = click.help_option('-h', '--help')(f)
    #     # f = click.version_option(__version__, '-v', '--version')(f)
    #     # f = debug_option(f)
    #     return f
    #
    # def AstroHub_cmd(*args, **kwargs):
    #     """
    #     Wrapper over click.command which sets common opts
    #
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #
    #     def inner_decorator(f):
    #         f = click.command(*args, **kwargs)(f)
    #         f = common_options(f)
    #         return f
    #
    #     return inner_decorator

    def dataSearch_name(self,name):
        if name:
            model_info = self.get_instance[1]
            res = []
            for i in model_info:
                if i['AstroHub']['name'] == name:
                    res.append(i)
            if len(res) == 0:
                return "No match results~"
            else:
                return self.filter_latest(res)
        else:
            raise ValueError(
                "Search function requires at least one parameter"
            )

    def compress_image(self,model_id,data_id):
        self.get_requirements(model_id)
        time.sleep(2)
        self.docker_file(model_id,data_id)
        self.build_image(model_id)

    def run(self,model_id,data_id,cpu,gpu,nodeName):
        self.compress_image(model_id,data_id)
        time.sleep(2)
        job = self.create_job_object(model_id,cpu=cpu,gpu=gpu,nodeName=nodeName)
        time.sleep(2)
        self.create_job(job)


    def get_task_status(self,model_id):
        return self.inspect_job_status(model_id)

    def get_task_result(self,model_id):
        return self.get_job_result(model_id)

    def get_task_log(self,jobName):
        pods = self.get_pods_by_job(jobName)
        print(pods)
        if pods:
            logs = self.core.read_namespaced_pod_log(pods[0], 'astrohub')
            print(logs)
        else:
            return 'No job running'






