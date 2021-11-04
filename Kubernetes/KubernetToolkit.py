from kubernetes import client,config

class KubernetTools:

    def __init__(self):
        config.load_kube_config(config_file="/Users/renyiming/kubernetes/kubeconfig.yaml")
        self.core = client.CoreV1Api()
        self.batch = client.BatchApi()


    def list_Namespace(self):
        data = []
        for namespace in self.core.list_namespace().items:
            data.append(namespace.metadata.name)
        return data

    def create_Namespace(self, name):
        body = client.V1Namespace()
        body.metadata = client.V1ObjectMeta(name=name)
        # print(body)
        return self.core.create_namespace(body=body)

    def delete_Namespace(self,name):
        body = client.V1Namespace()
        body.metadata = client.V1ObjectMeta(name=name)
        return self.core.delete_namespace(name,body=body)


    def create_node(self,name):
        body = client.V1Node()
        body.metadata = client.V1ObjectMeta(name=name)
        return self.core.create_node(body=body)

    def delete_node(self,name):
        body = client.V1Node()
        body.metadata = client.V1ObjectMeta(name=name)
        return self.core.delete_node(name,body=body)

    def get_all_nodes(self):
        nodes = self.core.list_node()
        res = []
        for item in nodes.items:
            res.append({
                'name': item.metadata.name,
                'labels':item.metadata.labels,
                'addresses':item.status.addresses,
                'allocatable_cpu':item.status.allocatable,
                'node_info':item.status.node_info
            })
        return res


    def list_pod(self,namespace,getAll):
        if getAll == True:
            return self.core.list_pod_for_all_namespaces()
        else:
            return len(self.core.list_namespaced_pod(namespace=namespace).items)

