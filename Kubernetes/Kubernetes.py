from kubernetes import client, config
from kubernetes.watch import Watch
from .KubernetToolkit import KubernetTools
import time

class KubernetClient(KubernetTools):

    def __init__(self):
        config.load_kube_config(config_file="/Users/renyiming/kubernetes/kubeconfig.yaml")
        self.core = client.CoreV1Api()
        self.batch = client.BatchV1Api()

    def create_job_object(self,uuid,cpu,gpu,nodeName):
        resources = client.V1ResourceRequirements(
            limits={'cpu':cpu,'alpha.kubernetes.io/nvidia-gpu':gpu}
        )
        container = client.V1Container(
            name=uuid,
            image= 'astrohub:'+uuid,
            # image="testx",
            image_pull_policy= 'Never',
            resources=resources,
            command=["/bin/bash","-c","pip3 install *.whl;python3 MLP.py"])
                     # 'python3 ' + model_name + '.py'])
            # args=
        if nodeName:
            podSpec = client.V1PodSpec(restart_policy="Never", containers=[container], node_name=nodeName)
        else:
            podSpec = client.V1PodSpec(restart_policy="Never", containers=[container])

        template = client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"astrohub": uuid}),
            spec=podSpec)

        spec = client.V1JobSpec(
            template=template,
            # parallelism= parallel_times,
            backoff_limit=4)

        job = client.V1Job(
            api_version="batch/v1",
            kind="Job",
            metadata=client.V1ObjectMeta(name=uuid),
            spec=spec)
        print('Kubernetes Job created')
        return job


    def create_job(self,job):
        namespaces = self.list_Namespace()
        if 'astrohub' not in namespaces:
            self.create_Namespace('astrohub')
        jobs = self.list_job()
        if job.metadata.name in jobs.keys():
            return "Jobs batch " +job.metadata.name + " already exists"
        else:
            responce =self.batch.create_namespaced_job(body=job,namespace='astrohub')
            print('Kubernestes Job starting!')
        return responce


    def inspect_job_status(self,jobName):
        if not self.list_job().keys():
            print('No job exists')
            return

        inspector = Watch()
        for status in inspector.stream(
            func=self.batch.list_namespaced_job,
            namespace='astrohub',
            label_selector=f'job-name={jobName}'
        ):
            st = status['object'].status
            if st.active == 1 and st.failed == None and st.succeeded == None:
                return 'Running~~~,Please wait~'
            elif st.failed == 1:
                return 'Job failed, Please check logs'
            elif st.succeeded == 1:
                return 'Completed'

    # def inspect_job_status(self,jobName):
    #     status = self.batch.read_namespaced_job_status(jobName,'astrohub')

    def get_job_result(self,jobName):
        pods = self.get_pods_by_job(jobName)
        if pods:
            if self.inspect_job_status(jobName) == 'Completed':
                logs = self.core.read_namespaced_pod_log(pods[0],'astrohub')
                log_lis = logs.split('\n')
                result = ''
                for log in log_lis[-6:]:
                    result += log + '\n'
                return result
            else:
                return "Job's not complete,Please wait"
        else:
            return 'No job running'



    def list_job(self):
        jobs = self.batch.list_namespaced_job(namespace='astrohub')
        job_dict = {}
        for item in jobs.items:
            jobName = item.metadata.name
            related_pods = self.get_pods_by_job(jobName)
            job_dict.update({jobName:related_pods})
        return job_dict


    def get_pods_by_job(self,jobName):
        related_pods = self.core.list_namespaced_pod(
            namespace='astrohub',
            label_selector=f'job-name={jobName}'
        )
        pods = []
        for item in related_pods.items:
            pods.append(item.metadata.name)
        return pods


    def delete_job(self,jobName,remove_all):
        jobs = self.list_job()
        if jobName not in jobs.keys():
            return "Job batch '" +jobName + "' does not exist"
        else:
            if remove_all == True:
                return self.batch.delete_collection_namespaced_job('astrohub')
            else:
                return self.batch.delete_namespaced_job(
                    namespace='astrohub',
                    name=jobName,
                    propagation_policy='Background'
                )



# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config(config_file="/Users/renyiming/kubernetes/kubeconfig.yaml")
#
# v1 = client.CoreV1Api()
# print("Listing pods with their IPs:")
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
# a = KubernetClient()
# print(a.delete_job('test',False))
# job = a.create_job_object('d400a239-c252-4fec-bf17-a9ded50729ba',1,0,'')
# # print(job)
# print(a.create_job(job))
# print(a.get_pods_by_job('d400a239-c252-4fec-bf17-a9ded50729ba'))
# print(a.get_job_result('test'))
# print(a.inspect_job_status('d400a239-c252-4fec-bf17-a9ded50729ba'))
# print(a.create_job('astrohub'))